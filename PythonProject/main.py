# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
import random


def guess_number():
    # 生成随机数字（1-100）
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    score = 100

    print("欢迎来到猜数字游戏！")
    print(f"我已经想好了1-100之间的数字，你有{max_attempts}次机会猜哦")

    while attempts < max_attempts:
        try:
            guess = int(input("请输入你的猜测: "))
        except:
            print("请输入有效的数字！")
            continue

        attempts += 1

        if guess == secret:
            print(f"恭喜你！在第{attempts}次猜对了！")
            print(f"你的最终得分：{score}")
            return
        elif guess < secret:
            print("猜小了，再试一次！")
        else:
            print("猜大了，再试一次！")

        # 每次扣分机制
        score -= 15
        if score < 0:
            score = 0

        # 显示剩余次数
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"剩余次数：{remaining}次，当前得分：{score}")

    print(f"游戏结束，正确数字是：{secret}")


# 启动游戏
guess_number()