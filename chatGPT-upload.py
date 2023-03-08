# coding=utf-8
import os
import openai

# 目前需要设置代理才可以访问 api
os.environ["HTTP_PROXY"] = "127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "127.0.0.1:7890"

openai.api_key = "这里粘贴你的api-key"

print("这是一个demo")

exit1 = None
while 1 == 1:
    if exit1 == 'N' or exit1 == 'n':
        exit()
    else:
        user_input = input("请输入你想问的问题: ")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                # {"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"},
                {"role": "user", "content": user_input}
            ]
        )
        print(completion.choices[0].message.content)
        exit1 = input("是否继续沟通?不沟通请输入N:(Y/n) ")
