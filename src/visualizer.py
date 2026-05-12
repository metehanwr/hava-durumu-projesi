
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

GRAFIK_KLASORU = os.path.join("outputs", "graphs")


class Visualizer:
    def __init__(self, veri):
        self.veri = veri
        os.makedirs(GRAFIK_KLASORU, exist_ok=True)

    def aylik_sicaklik(self):

        aylik = self.veri.groupby("ay")["sicaklik"].mean()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(aylik.index, aylik.values, marker="o", color="tomato", linewidth=2)
        ax.set_title("Aylık Ortalama Sıcaklık")
        ax.set_xlabel("Ay")
        ax.set_ylabel("Sıcaklık (°C)")
        ax.grid(True, linestyle="--", alpha=0.5)
        fig.tight_layout()
        fig.savefig(os.path.join(GRAFIK_KLASORU, "01_sicaklik.png"), dpi=150)
        plt.close(fig)
        print("Grafik kaydedildi: 01_sicaklik.png")


    def yagis_dagilimi(self):

        aylik = self.veri.groupby("ay")["yagis"].sum()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(aylik.index, aylik.values, color="steelblue", edgecolor="white")
        ax.set_title("Aylık Toplam Yağış")
        ax.set_xlabel("Ay")
        ax.set_ylabel("Yağış (mm)")
        ax.grid(axis="y", linestyle="--", alpha=0.5)
        fig.tight_layout()
        fig.savefig(os.path.join(GRAFIK_KLASORU, "02_yagis.png"), dpi=150)
        plt.close(fig)
        print("Grafik kaydedildi: 02_yagis.png")


    def uret(self):
        self.aylik_sicaklik()
        self.yagis_dagilimi()
