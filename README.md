<div align="center">

<p align="center">
    <img src="https://user-images.githubusercontent.com/81006731/227700420-8083b21d-4518-4546-a956-2f68d92bd28e.png" alt="" width="300px">
</p>
    
# QQ 群聊美少女语音AI
    
_✨ 基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 以及 [VITS-fast-fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning) + [revChatGPT](https://github.com/acheong08/ChatGPT)  实现 ✨_  
    
Combination of ChatGPT and VITs anime girl AI voice and used in QQ robot
    
</div>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-blue" alt="license">
</p>


#### 介绍
 ChatGPT 和 VITS 二次元美少女AI语音 结合 并用于 QQ聊天机器人 | Combination of ChatGPT and VITs anime girl AI voice and used in QQ robot
 
#### 由于ChatGPT 对国内彻底上墙了，因此该项目会利用开源模型ChatGLM 做本地化版本
（ChatGLM本地化版本）QQ 语音化美少女AI 项目仓库：[ChatGLM_VITS_For_QQ-Rob](https://github.com/Panzer-Jack/ChatGLM_VITS_For_QQ-Rob) 

<h2 style="color:red">注意: </h2>
<ul style="color:red">
    <li>1· 你的python版本为 3.8</li>
    <li>2· 你需要下载你操作系统相对于的go-cqhttp文件并放置到根目录里，你可以在后面索引1中去下载</li>
    <li>3· 你需要安装的requirements中的依赖库</li>
    <li>4· 你需要将语音模型放置到根目录中, 并重命名为: G_latest.pth, 这里你可以参考后面的索引2</li>
    <li>5. 如果你在配置chatGPT过程中出现问题可以去参考索引3</li>
</ul>

### 索引：
1. [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 

2. [VITS-fast-fine-tuning](https://github.com/Plachtaa/VITS-fast-fine-tuning)

3. [revChatGPT](https://github.com/acheong08/ChatGPT)


#### 软件架构说明
1. config.py 设置机器人语言和声音模型 以及 chatGPT 的身份令牌
2. run_server.py 为启动主文件


#### 安装教程

1.  安装go-cqhttp相应系统版本并将其放置到 项目文件夹根目录 中
2.  将你的 语言模型重命名为: G_latest.pth 放置到 项目文件夹根目录 中
3.  安装相关依赖库
4.  注册一个OpenAI账号来得到chatGPT的Access token并将其填写到 config.py 的access_token中
(登录chatGPT官网后 访问: https://chat.openai.com/api/auth/session 来获取Access token)


#### 使用说明

· 安装好相关运行环境。                   

· 在项目根目录的config.py中设定声音模型和语言以及ChatGPT身份令牌

· 开启go-cqhttp 来监听QQ消息

· 打开控制台 移动到项目文件夹更目录输入:
1.  ```pip3 install -r requirements.txt```
2.  ```python3 run_server ```

#### 项目现状

1. 目前只做了QQ群聊中匹配, 你可以通过@机器人 来让机器人来读取你的信息

2. 项目目前还在不断完善中。。。

