"""
    作者:北辰
    功能:BMR 计算器
    版本:2.0
    日期:12/06/2018
    2.0新增功能:提示用户输入并且直到用户选择退出
"""

def main():
    """
    主函数
    """
    y_or_n = input('是否退出程序(y/n)? ')

    while y_or_n != 'y':
        # 性别
        gender = input('性别: ')
        # 体重(kg)
        weight = float(input('体重(kg): '))
        # 身高(cm)
        height = float(input('身高(cm): '))
        # 年龄
        age = int(input('年龄: '))
        if gender=='男':
            # 男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender=='女':
            # 女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1
        if bmr != -1:
            print('基础代谢率(大卡), ',bmr)
        else:
            print('暂不支持该性别!')
        print()      #输出空行
        y_or_n = input('是否退出程序(y/n)? ')


if __name__=='__main__':
    main()