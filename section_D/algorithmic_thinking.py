salary = int(input("Enter your salary: "))
if salary >= 50000:
    bonus = 0.1 * salary
    total_sal = salary + bonus
    print("Bonus: {}" .format(bonus))
    print("Total Salary: {}" .format(total_sal))
    
else:
    bonus = 0.2 * salary
    total_sal = salary + bonus
    print("Bonus: {}" .format(bonus))
    print("Total Salary: {}" .format(total_sal))
