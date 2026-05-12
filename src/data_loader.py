
import pandas as pd


class DataLoader:
    def __init__(self, dosya_yolu):
        self.dosya_yolu = dosya_yolu
        self.veri = None

    def yukle(self):
        try:
            self.veri = pd.read_csv(self.dosya_yolu, parse_dates=["tarih"])
            print(f"Veri yüklendi: {len(self.veri)} satır")
            return self.veri
        except FileNotFoundError:
            print(f"HATA: Dosya bulunamadı -> {self.dosya_yolu}")
            raise

    def temizle(self):
        df = self.veri.copy()

        print(f"Eksik veri: {df.isnull().sum().sum()}")

        df.fillna(df.median(numeric_only=True), inplace=True)

        df["ay"] = df["tarih"].dt.month

        self.veri = df
        print("Veri temizlendi.")
        return self.veri
