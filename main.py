from datetime import datetime, timedelta
import os
import sys

def clear_screen():
    """清屏函数"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """打印程序标题"""
    print("=" * 60)
    print("           日期和保质期推测过期日程序")
    print("=" * 60)

def get_current_date():
    """获取当前日期输入"""
    while True:
        print("\n请输入当前日期:")
        print("格式: YYYY-MM-DD (例如: 2023-10-01)")
        print("或直接按回车使用今天日期")
        
        current_date_str = input(">> ").strip()
        
        # 如果用户直接按回车，使用今天日期
        if not current_date_str:
            current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            print(f"使用今天日期: {current_date.strftime('%Y年%m月%d日')}")
            return current_date
        
        # 验证日期格式
        try:
            current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
            return current_date
        except ValueError:
            print("❌ 日期格式错误，请按照 YYYY-MM-DD 格式输入")

def get_shelf_life():
    """获取保质期输入"""
    while True:
        print("\n请输入保质期:")
        print("格式: 数字+单位")
        print("示例: 30天, 6个月, 1年, 2周")
        
        shelf_life_input = input(">> ").strip()
        
        try:
            # 分离数字和单位
            import re
            match = re.match(r'^\s*(\d+)\s*(\D+)\s*$', shelf_life_input)
            if not match:
                print("❌ 格式错误，请按照示例格式输入")
                continue
                
            number = int(match.group(1))
            unit = match.group(2).strip().lower()
            
            # 根据单位计算保质期天数
            if unit in ['天', '日', 'days', 'day', 'd']:
                days = number
                unit_display = f"{number}天"
            elif unit in ['周', 'weeks', 'week', 'w']:
                days = number * 7
                unit_display = f"{number}周"
            elif unit in ['月', 'months', 'month', 'm']:
                # 使用近似值计算月份
                days = number * 30
                unit_display = f"{number}个月"
            elif unit in ['年', 'years', 'year', 'y']:
                # 使用近似值计算年份
                days = number * 365
                unit_display = f"{number}年"
            else:
                print("❌ 单位不支持，请使用天、周、月或年")
                continue
                
            return days, unit_display
        except ValueError:
            print("❌ 输入格式错误，请重新输入")

def calculate_expiry_date():
    """
    通过输入当前日期和保质期推测过期日
    """
    print_header()
    
    # 获取当前日期
    current_date = get_current_date()
    
    # 获取保质期
    days, unit_display = get_shelf_life()
    
    # 计算过期日
    expiry_date = current_date + timedelta(days=days)
    
    # 清屏并显示结果
    clear_screen()
    print_header()
    print("\n                 📊 计算结果 📊")
    print("=" * 50)
    print(f"📅 当前日期: {current_date.strftime('%Y年%m月%d日')}")
    print(f"📦 保质期: {unit_display}")
    print(f"⏰ 过期日: {expiry_date.strftime('%Y年%m月%d日')}")
    
    # 计算剩余天数
    days_remaining = (expiry_date - current_date).days
    print(f"📋 剩余天数: {days_remaining}天")
    
    # 根据剩余天数给出提示
    print("\n" + "=" * 40)
    if days_remaining <= 0:
        print("⚠️  警告: 该产品已过期！")
    elif days_remaining <= 7:
        print("⚠️  警告: 该产品即将过期，请尽快使用！")
    elif days_remaining <= 30:
        print("⚠️  提示: 该产品将在一个月内过期，请注意使用时间！")
    else:
        print("✅ 该产品在保质期内")
    print("=" * 40)

def main():
    """
    主函数，控制程序流程
    """
    while True:
        try:
            calculate_expiry_date()
            
            # 询问是否继续
            print("\n是否继续计算?")
            print("1. 是 (Y/1)")
            print("2. 否 (N/2)")
            
            continue_choice = input(">> ").strip().lower()
            if continue_choice in ['n', 'no', '2', '否', '退出', 'exit']:
                print("\n感谢使用，再见！")
                break
            else:
                clear_screen()
                
        except KeyboardInterrupt:
            print("\n\n程序被用户中断")
            break
        except Exception as e:
            print(f"\n发生错误: {e}")
            input("按回车键继续...")
            clear_screen()

if __name__ == "__main__":
    main()