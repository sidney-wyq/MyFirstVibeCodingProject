# -*- coding: utf-8 -*-
"""Python 基础演示：基本数据类型与控制语句"""


# ==================== 一、基本数据类型 ====================

def demo_data_types():
    # 1. 整数（int）
    age = 25
    big_number = 123_456_789  # 可用下划线分隔，便于阅读
    print("int:", age, big_number, type(age))

    # 2. 浮点数（float）
    price = 19.99
    scientific = 3.5e-2  # 科学计数法，即 0.035
    print("float:", price, scientific, type(price))

    # 3. 复数（complex）
    c = 3 + 4j
    print("complex:", c, "模 =", abs(c))

    # 4. 布尔值（bool）
    is_student = True
    print("bool:", is_student, type(is_student))

    # 5. 字符串（str）
    name = "Alice"
    greeting = f"你好，{name}！今年 {age} 岁"  # f-string 格式化
    print("str:", greeting, type(name))

    # 字符串常用操作
    s = "Hello Python"
    print("字符串长度:", len(s))
    print("转大写:", s.upper())
    print("切片 s[0:5]:", s[0:5])
    print("分割:", s.split(" "))

    # 6. 列表（list）—— 可变、有序
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    fruits[1] = "grape"
    print("list:", fruits, type(fruits))

    # 7. 元组（tuple）—— 不可变、有序
    point = (3, 4)
    x, y = point  # 解包
    print("tuple:", point, "解包后 x =", x, ", y =", y)

    # 8. 字典（dict）—— 键值对
    person = {"name": "Alice", "age": 25, "city": "北京"}
    person["email"] = "alice@example.com"
    print("dict:", person)
    print("访问键 name:", person["name"])
    print("遍历字典:")
    for key, value in person.items():
        print(f"  {key} -> {value}")

    # 9. 集合（set）—— 无序、不重复
    numbers = {1, 2, 2, 3, 3, 3}
    print("set（自动去重）:", numbers, type(numbers))

    # 10. None 类型
    nothing = None
    print("NoneType:", nothing, type(nothing))

    # 类型转换
    print("类型转换: int('42') =", int("42"),
          "| float('3.14') =", float("3.14"),
          "| str(100) =", str(100))


# ==================== 二、控制语句 ====================

def demo_control_statements():
    # 1. if / elif / else 条件语句
    score = 85
    if score >= 90:
        grade = "优秀"
    elif score >= 80:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "不及格"
    print(f"\n条件语句：分数 {score} -> 等级 {grade}")

    # 三元表达式
    parity = "偶数" if score % 2 == 0 else "奇数"
    print(f"三元表达式：{score} 是{parity}")

    # 2. for 循环 + range
    print("\nfor 循环（range 1~5 的平方）:")
    for i in range(1, 6):
        print(f"  {i} 的平方 = {i ** 2}")

    # 3. while 循环
    print("\nwhile 循环（计算 1+2+...+10）:")
    total, n = 0, 1
    while n <= 10:
        total += n
        n += 1
    print("  结果 =", total)

    # 4. break 与 continue
    print("\nbreak/continue（找 10 以内第一个大于 5 的偶数）:")
    for i in range(1, 11):
        if i <= 5:
            continue  # 跳过 5 及以下的数
        if i % 2 == 0:
            print("  找到:", i)
            break  # 找到后立即退出循环

    # 5. 嵌套循环：九九乘法表（部分）
    print("\n嵌套循环（3x3 乘法表）:")
    for i in range(1, 4):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i * j}", end="\t")
        print()  # 换行

    # 6. for-else 语句
    print("\nfor-else（判断质数）:")
    num = 13
    for i in range(2, num):
        if num % i == 0:
            print(f"  {num} 不是质数，能被 {i} 整除")
            break
    else:
        print(f"  {num} 是质数")  # 循环正常结束（未 break）时执行

    # 7. match 语句（Python 3.10+）
    print("\nmatch 语句:")
    command = "add"
    match command:
        case "add":
            print("  执行添加操作")
        case "delete":
            print("  执行删除操作")
        case "add" | "update":  # 多模式匹配
            print("  执行更新操作")
        case _:
            print("  未知命令")

    # 8. enumerate 与 zip
    print("\nenumerate / zip:")
    fruits = ["苹果", "香蕉", "樱桃"]
    prices = [5.5, 3.0, 8.0]
    for idx, fruit in enumerate(fruits, start=1):
        print(f"  {idx}. {fruit}")
    for fruit, price in zip(fruits, prices):
        print(f"  {fruit} 单价 {price} 元")


if __name__ == "__main__":
    print("=" * 30, "基本数据类型", "=" * 30)
    demo_data_types()
    print("\n" + "=" * 30, "控制语句", "=" * 30)
    demo_control_statements()
