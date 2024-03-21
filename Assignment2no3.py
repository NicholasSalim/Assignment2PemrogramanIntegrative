class BMI_Calculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)


weight = float(input("Masukkan berat Anda (kg): "))
height = float(input("Masukkan tinggi Anda (meter): "))

# Membuat objek 
person = BMI_Calculator(weight, height)

# Menghitung BMI
bmi = person.BMI_Value()

print(f" Berat Anda adalah {weight} kg dan tinggi Anda adalah {height} meter.")
print(f"Nilai BMI Anda adalah: {bmi:.2f}")
