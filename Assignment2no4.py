grades = []


while True:
    grade = int(input("Masukkan nilai (atau -1 untuk mengakhiri): "))
    if grade == -1:
        break
    grades.append(grade)

# Menghitung rata-rata nilai
average = sum(grades) // len(grades)

print("Rata-rata:", average)

for grade in grades:
    print(grade)
