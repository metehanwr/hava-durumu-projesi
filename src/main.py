
import os
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(KOK, "src"))
os.chdir(KOK)

from data_loader   import DataLoader
from analyzer      import DataAnalyzer
from visualizer    import Visualizer
from model_trainer import ModelTrainer


def rapor_kaydet(istatistikler, metrikler):
    os.makedirs(os.path.join("outputs", "reports"), exist_ok=True)
    yol = os.path.join("outputs", "reports", "rapor.txt")
    with open(yol, "w", encoding="utf-8") as f:
        f.write("HAVA DURUMU PROJESİ RAPORU\n")
        f.write("="*40 + "\n\n")
        f.write("NumPy İstatistikleri:\n")
        for k, v in istatistikler.items():
            f.write(f"  {k}: {v}\n")
        f.write("\nModel Sonuçları:\n")
        for k, v in metrikler.items():
            f.write(f"  {k}: {v}\n")
    print(f"\nRapor kaydedildi: {yol}")


def ozet_yazdir(veri):

    print("\n--- Veri Özeti ---")
    print(f"Toplam kayıt : {len(veri)}")
    print(f"Tarih aralığı: {veri['tarih'].min().date()} → {veri['tarih'].max().date()}")
    print(veri[["sicaklik", "nem", "yagis"]].describe().round(2))


def dogrula(veri):

    hatalar = []
    if (veri["nem"] < 0).any() or (veri["nem"] > 100).any():
        hatalar.append("Nem değerleri hatalı!")
    if (veri["yagis"] < 0).any():
        hatalar.append("Negatif yağış var!")
    if hatalar:
        for h in hatalar:
            print(f"UYARI: {h}")
    else:
        print("Veri doğrulama: OK")


def main():
    print("=== ADIM 1: VERİ YÜKLEME ===")
    yukleyici = DataLoader(os.path.join(KOK, "data", "hava_durumu.csv"))
    veri = yukleyici.yukle()
    veri = yukleyici.temizle()
    ozet_yazdir(veri)
    dogrula(veri)

    print("\n=== ADIM 2: ANALİZ ===")
    analizci = DataAnalyzer(veri)
    istatistikler = analizci.numpy_istatistikler()
    analizci.pandas_ozet()

    print("\n=== ADIM 3: GRAFİKLER ===")
    gorsellestirici = Visualizer(veri)
    gorsellestirici.uret()

    print("\n=== ADIM 4: MODEL ===")
    egitici = ModelTrainer(veri)
    metrikler = egitici.egit_ve_degerlendir()

    print("\n=== ADIM 5: RAPOR ===")
    rapor_kaydet(istatistikler, metrikler)

    print("\nProje tamamlandı!")
    print("  Grafikler : outputs/graphs/")
    print("  Rapor     : outputs/reports/rapor.txt")


if __name__ == "__main__":
    main()
