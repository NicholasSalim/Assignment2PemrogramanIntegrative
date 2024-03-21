total = 0

while True:
    num = float(input("Masukkan angka (atau -1 untuk berhenti): "))
    if num == -1:
        break
    total += num

print(f"Total: {total:.2f}")
