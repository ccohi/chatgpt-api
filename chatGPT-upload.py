# coding=utf-8
import argparse
import os
import openai


def parse_args():
    """

    :return: 进行参数解析
    """
    description = "你需要添加一下几个参数：[-a api | -p 本地代理端口号]"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-a', '--api', metavar='', help=":api的接口号码")
    parser.add_argument('-p', '--port', metavar='', help=":本地代理端口号")
    # parser.add_argument('-q', '--question', metavar='', help=":想提问的问题")
    args = parser.parse_args()
    parser.print_help()
    return args


def chat():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    print(completion.choices[0].message.content)


if __name__ == '__main__':
    banner = """
    welcome to use chatGPT-api!

         ######  ##     ##    ###  #########        version v1.0  author:ccohi
    ##    ## ##     ##   ## ##      ##            ##    ##  ##     ##  ##
    ##       ##     ##  ##   ##     ##            ##        ##     ##  ##
    ##       ######### ##     ##    ##    ####### ##   #### ########   ##
    ##       ##     ## #########    ##            ##    ##  ##         ##
    ##    ## ##     ## ##     ##    ##            ##    ##  ##         ##
     ######  ##     ## ##     ##    ##             ######   ##        ####
        """
    print(banner)

    args = parse_args()
    if args.port is None and args.api is None:
        print("***程序已退出,请输入参数后重试***")
    else:
        # 目前需要设置代理才可以访问 api
        os.environ["HTTP_PROXY"] = "127.0.0.1:" + args.port
        os.environ["HTTPS_PROXY"] = "127.0.0.1:" + args.port

        openai.api_key = args.api

        print("~~~~~~~你好我是人工智能AI模型chatGPT，您有任何问题都可以问我哦~~~~~~~")

        exit1 = None
        while 1 == 1:
            if exit1 == 'N' or exit1 == 'n':
                exit()
            else:
                user_input = input("请输入你想问的问题: ")
                chat()
                exit1 = input("是否继续沟通?不沟通请输入N:(Y/n) ")
