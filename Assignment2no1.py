from datetime import datetime, timedelta

def print_future_date(days):
    # Mendapatkan tanggal hari ini
    today = datetime.today()
    
    # Menambahkan jumlah hari yang diinputkan ke tanggal hari ini
    future_date = today + timedelta(days=days)
    
   
    hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    
    
    bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    
    # Mencetak tanggal dalam format yang diminta
    print(f"{hari[future_date.weekday()]}, {future_date.strftime('%d')} {bulan[future_date.month - 1]} {future_date.strftime('%Y')}")

# Input jumlah hari dari pengguna
jumlah_hari = int(input("Masukkan jumlah hari: "))

# Memanggil fungsi untuk mencetak tanggal di masa depan
print_future_date(jumlah_hari)
