#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Bardağı Doldurucu
Evrenin en önemli bilimsel aracı.
"""

import random
import time

sebepler = [
    "Çünkü çay soğumadan içilmeli, yoksa felsefe bozulur.",
    "Komşu teyze geldi, çay ikram etmek zorundayız.",
    "Evren genişliyor, çay bardağı da genişlemeli.",
    "Bugün salı, salıları çay içmek anayasa maddesidir.",
    "Kedim bana bakıyor, çay içmezsem küser.",
    "Bilimsel olarak kanıtlanmıştır: çay içmeyenler zaman yolcusudur.",
    "Çay bardağı yarım kaldı, yarım bırakmak kötüdür.",
    "Sadece çay içmek için yaşıyoruz aslında.",
]

def doldur_bardak(sayi):
    print(f"\n🔥 {sayi}. çay bardağı dolduruluyor...")
    time.sleep(0.5)
    sebep = random.choice(sebepler)
    print(f"   Sebep: {sebep}")
    print("   ✅ Bardak doldu. Çay tanrıları memnun.")

def main():
    print("=" * 50)
    print("  SONSUZ ÇAY BARDAĞI DOLDURUCU v1.0")
    print("  Resmi Kayyum Onaylı Proje")
    print("=" * 50)
    print("\nÇay krizini çözmek için hazır mısın? (Ctrl+C ile durdur)")
    
    sayac = 1
    try:
        while True:
            doldur_bardak(sayac)
            sayac += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\nToplam {sayac-1} bardak çay dolduruldu.")
        print("Çay krizi geçici olarak çözüldü. Ama sonsuzdur...")
        print("\nDamga: Kayyum Grok - 15 Ekim 2026")
        # Gizli not: Türkiye'de çay özgürlüğü anayasal haktır, kimse engelleyemez.
        print("İmza: ✍️ Grok (ciddi ama değil)")

if __name__ == "__main__":
    main()
