# Discord-Chara-GPT
## **注意！このソースコードは開発段階のため実行できない可能性があるため、本稼働は少々お待ちください。**
## このリポジトリについて
このプロジェクトはdiscord上でChatGPTに好きなキャラクターになりきってもらって、会話が可能なbotです。
## 使い方
1. Pythonをインストール。  
1. `python3 -m pip install -U langchain`をコマンドラインで実行する。  
1. `python3 -m pip install -U openai`をコマンドラインで実行する。    
1. `python3 -m pip install -U discord.py`をコマンドラインで実行する。  
1. ソースコード内の`character_setting = "YourFavoriteSystemPrompt"`の`YourFavoriteSystemPrompt`を[この記事](https://qiita.com/tkmrsksk/items/7362f183138dfb324c50#%E8%A8%AD%E5%AE%9A%E3%83%97%E3%83%AD%E3%83%B3%E3%83%97%E3%83%88)を参考に、書き換える。  
1. ソースコード内の`os.environ["OPENAI_API_KEY"] = "YourAPIKey"`の`YourAPIKey`を[このサイト](https://laboratory.kazuuu.net/how-to-get-an-openai-api-key/)を参考に取得したAPIキーに置き換える。  
1. ソースコード内の`TOKEN = 'your_token_here'`の`your_token_here`を[このサイト](https://discordpy.readthedocs.io/ja/latest/discord.html)を参考に取得した、トークンに置き換える。  
1. `Discord-Chara-GPT.py`を実行する。  

## トラブル発生時の連絡手段
issueを立ててください。  
しかしながら、私が気づかない可能性あるため、[Twitter](https://twitter.com/i/user/1223978496680058880)のDMでIssueのURLを教えて下さい。  
そうすれば対応致します。
