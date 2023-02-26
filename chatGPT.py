from revChatGPT.V1 import Chatbot
from Vits_vioce_API import vits_voice
import config


chatbot = Chatbot(config={
    "access_token": config.access_token
})

prev_text = ""


def chatGPT_ask(prompt, prev_text=prev_text):
    for data in chatbot.ask(
            prompt,
    ):
        message = data["message"][len(prev_text):]
        print(message, end="", flush=True)
        prev_text = data["message"]
    print("\n")
    vits_voice(txt=prev_text, speaker=78, language=0)


print()

# 78 柚子社-宁宁
# 测试用：
# chatGPT_ask(prompt="你好啊！请你用日语来回答")
# vits_voice(txt='FTPサーバーを構成するための機能が組み込まれています。', speaker=79, language=0)
