"""
输入学生考试成绩计算平均分

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""

import os
import time


def main():
    string = 'Welcome to 1000 Phone Chengdu Campus      '
    while True:
        print(string)
        time.sleep(0.2)
        string = string[1:] + string[0:1]
        # for Windows use os.system('cls') instead
        os.system('cls')  # os.system('clear')


if __name__ == '__main__':
    main()
