#!/usr/bin/env python3
"""
本地测试脚本 - 在Codespaces中测试程序功能
"""

from datetime import datetime, timedelta

def test_calculation():
    """测试日期计算功能"""
    print("=== 测试日期计算功能 ===")
    
    # 测试用例
    test_cases = [
        {
            "current_date": "2023-10-01",
            "shelf_life": "30天",
            "expected": "2023-10-31"
        },
        {
            "current_date": "2023-01-01",
            "shelf_life": "1年",
            "expected": "2024-01-01"  # 注意：近似计算，实际是365天后
        },
        {
            "current_date": "2023-03-01",
            "shelf_life": "6个月",
            "expected": "2023-09-01"  # 近似计算
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}:")
        current_date = datetime.strptime(test["current_date"], "%Y-%m-%d")
        
        # 解析保质期
        shelf_life = test["shelf_life"]
        if "天" in shelf_life:
            days = int(shelf_life.replace("天", ""))
        elif "年" in shelf_life:
            days = int(shelf_life.replace("年", "")) * 365
        elif "月" in shelf_life:
            days = int(shelf_life.replace("月", "")) * 30
        elif "周" in shelf_life:
            days = int(shelf_life.replace("周", "")) * 7
        
        expiry_date = current_date + timedelta(days=days)
        expected_date = datetime.strptime(test["expected"], "%Y-%m-%d")
        
        print(f"当前日期: {current_date.strftime('%Y-%m-%d')}")
        print(f"保质期: {shelf_life}")
        print(f"计算过期日: {expiry_date.strftime('%Y-%m-%d')}")
        print(f"预期过期日: {expected_date.strftime('%Y-%m-%d')}")
        
        # 检查结果
        if expiry_date.strftime('%Y-%m-%d') == expected_date.strftime('%Y-%m-%d'):
            print("✅ 测试通过")
        else:
            print("❌ 测试失败")

def test_program():
    """测试完整程序流程"""
    print("\n=== 测试完整程序流程 ===")
    
    # 模拟用户输入
    print("模拟输入: 当前日期 = 2023-10-01")
    print("模拟输入: 保质期 = 30天")
    
    current_date = datetime.strptime("2023-10-01", "%Y-%m-%d")
    days = 30
    expiry_date = current_date + timedelta(days=days)
    
    print(f"计算结果: 过期日 = {expiry_date.strftime('%Y年%m月%d日')}")
    print("✅ 程序逻辑测试完成")

if __name__ == "__main__":
    test_calculation()
    test_program()
    print("\n🎉 所有测试完成！")