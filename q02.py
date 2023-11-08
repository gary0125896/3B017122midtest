employee_records = []

print("-" * 28)
print("        員工薪資輸入        ")
print("    若姓名處未輸入則代表結束")
print("-" * 28)

# 輸入名稱
while True:
    name = input("請輸入姓名:")
    if not name:
        print("----------------------------")
        print("")
        print("----------------------------")
        print("----------------------------")
        print("")
        print("合計薪資：              0")
        print("平均薪資：              0.00")
        print("============================")
        break
    salary = float(input("請輸入薪資:"))
    print("")
    employee_records.append({"eName": name, "eSalary": salary})

print("-" * 28)
if employee_records:
    # 輸出員工薪資
    total_salary = 0
    for record in employee_records:
        name = record["eName"]
        salary = record["eSalary"]
        total_salary += salary
        print(f"員工{name} 的薪資為 {salary:,.0f}")

    # 平均薪資
    average_salary = total_salary / len(employee_records)

    # 輸出總計以及平均薪資
    print("-" * 28)
    print(f"合計薪資：{total_salary: >14,.0f}")
    print(f"平均薪資：   {average_salary: >14,.2f}")
    print("=" * 28)
else:
    raise SystemExit
