from pathlib import Path
import math

def total_salary(path):
    total = 0
    count = 0

    current_dir = Path(__file__).parent
    file_path = current_dir / "Department_payroll.txt"
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary_str = line.split(",")
                    total += float(salary_str.strip())
                    count += 1
                except ValueError:
                    continue
        average = total / count if count > 0 else 0
        return total, average

    except FileNotFoundError:
        print(f"Error: File <<Department_payroll.txt>> not found in the system")
        return 0, 0


total, average = total_salary("Department_payroll.txt",)
print(f"Total salary amount: {total}. Average salary: {average}")