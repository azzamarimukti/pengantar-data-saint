import pandas as pd

# Membuat DataFrame
data = {
    "Nama": ["Andi", "Budi", "Cici", "Dedi"],
    "Umur": [25, 30, 22, 28],
    "Kota": ["Jakarta", "Bandung", "Surabaya", "Medan"]
}

df = pd.DataFrame(data)

# Menampilkan data
print("DataFrame:")
print(df)
