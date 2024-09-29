def calculate_electricity_bill(units):
    # 定義每個用電區間的費率 (假設為住宅用電)
    rates = [
        (120, 1.63),  # 1-120 度，每度 1.63 元
        (330, 2.38),  # 121-330 度，每度 2.38 元
        (500, 3.52),  # 331-500 度，每度 3.52 元
        (700, 4.80),  # 501-700 度，每度 4.80 元
        (float('inf'), 5.66)  # 701 度以上，每度 5.66 元
    ]

    total_cost = 0
    remaining_units = units

    for limit, rate in rates:
        if remaining_units > 0:
            if remaining_units > limit:
                total_cost += limit * rate
                remaining_units -= limit
            else:
                total_cost += remaining_units * rate
                remaining_units = 0

    return total_cost

# 主程式
if __name__ == "__main__":
    try:
        units = float(input("請輸入用電量 (度): "))
        bill = calculate_electricity_bill(units)
        print(f"用電 {units} 度的電費為: {bill} 元")
    except ValueError:
        print("請輸入有效的數字。")