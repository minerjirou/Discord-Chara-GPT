import os
import discord

from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.base import CallbackManager

# Discordボットのトークン
TOKEN = 'your_token_here'

# APIキーの設定
os.environ["OPENAI_API_KEY"] = "YourAPIKey"

# 設定プロンプト
character_setting = "YourFavoriteSystemPrompt"

# チャットプロンプトテンプレート
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(character_setting),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# チャットモデル
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo", 
    max_tokens=512,
    temperature=0.2,
    streaming=True, 
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

# メモリ
memory = ConversationBufferWindowMemory(k=3, return_messages=True)

# 会話チェーン
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm, verbose=True)

# Discordボットの設定
client = discord.Client()

# Discordボットのイベント
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    response = conversation.predict(input=message.content)
    await message.channel.send(response)

client.run(TOKEN)
