"""
    作者:北辰
    功能:BMR 计算器
    版本:5.0
    日期:13/06/2018
    2.0新增功能:提示用户输入并且直到用户选择退出
    3.0新增功能:用户可以在一行输入所有信息,带单位的信息输出
    4.0新增功能:处理异常操作
    5.0新增功能:使程序模块化,将BMR计算功能封装到函数中
"""

def BMR_calculate(string_list):
    """
    计算BMR值
    """
    try:
        gender = string_list[0]
        weight = float(string_list[1])
        height = float(string_list[2])
        age = int(string_list[3])
        if gender == '男':
            # 男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1
        if bmr != -1:
            print('您的性别:{},体重:{}公斤,身高:{}厘米,年龄:{}岁'.format(gender, weight, height, age))
            print('您的基础代谢率:{}大卡'.format(bmr))
        else:
            print('暂不支持该性别!')
    except ValueError:
        print('请输入正确信息! ')
    except IndexError:
        print('输入信息过少! ')
    except:
        print('程序异常! ')

def main():
    """
    主函数
    """
    y_or_n = input('是否退出程序(y/n)? ')

    while y_or_n != 'y':
        print('请输入以下信息,用空格分割')
        input_str = input('性别 体重(kg) 身高(cm) 年龄: ')
        string_list = input_str.split(' ')
        BMR_calculate(string_list)
        print()      #输出空行
        y_or_n = input('是否退出程序(y/n)? ')


if __name__=='__main__':
    main()