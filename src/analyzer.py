
import numpy as np
import pandas as pd


class DataAnalyzer:
    def __init__(self, veri):
        self.veri = veri

    def numpy_istatistikler(self):

        sicaklik = np.array(self.veri["sicaklik"])
        yagis    = np.array(self.veri["yagis"])
        nem      = np.array(self.veri["nem"])

        sonuclar = {
            "ortalama_sicaklik": round(float(np.mean(sicaklik)), 2),
            "std_sicaklik":      round(float(np.std(sicaklik)), 2),
            "min_sicaklik":      round(float(np.min(sicaklik)), 2),
            "max_sicaklik":      round(float(np.max(sicaklik)), 2),
            "toplam_yagis":      round(float(np.sum(yagis)), 2),
            "korelasyon":        round(float(np.corrcoef(sicaklik, nem)[0, 1]), 4),
        }

        print("\n--- NumPy İstatistikleri ---")
        for k, v in sonuclar.items():
            print(f"  {k}: {v}")

        return sonuclar

    def pandas_ozet(self):
        print("\n--- Pandas Özet ---")
        print(self.veri[["sicaklik", "nem", "yagis"]].describe().round(2))

        aylik = self.veri.groupby("ay")["sicaklik"].mean().round(2)
        print(f"\nAylık ort. sıcaklık:\n{aylik}")

        return aylik
