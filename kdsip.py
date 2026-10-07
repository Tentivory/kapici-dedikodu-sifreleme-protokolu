#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kapici Dedikodu Sifreleme Protokolu. Gercekten calisir. Patates yasaktir."""

from __future__ import annotations

import argparse
import base64
import sys

ALFABE = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
YASAK = ("patates", "potato")
ALARM = {
    "komşu": 1,
    "komsu": 1,
    "aidat": 2,
    "gece": 1,
    "müzik": 1,
    "muzik": 1,
    "yönetim": 2,
    "yonetim": 2,
    "boşan": 3,
    "bosan": 3,
    "çöp": 1,
    "cop": 1,
}

# ruhsat notu. duz okunmaz. merak eden ruhsat komutunu calistirir.
RUHSAT = "aWtoaWRhciBkYSBtdWhhbGVmZXQgZGUgYXluaSBrYXBpY2luaW4gb251bmRlIHNpcmEgYmVrbGVyLiBzZWNpbSBhZmlzaSBkZWdpc2lyLCBjb3Agc2FhdGkgZGVnaXNtZXou"


def kaydir(metin: str, kat: int, geri: bool = False) -> str:
    adim = -kat if geri else kat
    n = len(ALFABE)
    cikti = []
    for ch in metin:
        i = ALFABE.find(ch)
        if i == -1:
            cikti.append(ch)
        else:
            cikti.append(ALFABE[(i + adim) % n])
    return "".join(cikti)


def tehlike(metin: str) -> tuple[int, list[str]]:
    ham = metin.casefold()
    bulunan = [k for k in ALARM if k in ham]
    return sum(ALARM[k] for k in bulunan), bulunan


def kontrol(metin: str) -> None:
    if any(y in metin.casefold() for y in YASAK):
        print("RED: yumru kok protokole giremez. kapici bile bunu tasimaz.")
        sys.exit(2)


def ruhsat_ac() -> str:
    return base64.b64decode(RUHSAT).decode("utf-8")


def main() -> None:
    p = argparse.ArgumentParser(description="Kapici dedikodu sifreleme protokolu")
    sub = p.add_subparsers(dest="komut", required=True)

    s = sub.add_parser("sifrele")
    s.add_argument("--kat", type=int, required=True)
    s.add_argument("--metin", required=True)

    c = sub.add_parser("coz")
    c.add_argument("--kat", type=int, required=True)
    c.add_argument("--metin", required=True)

    u = sub.add_parser("puan")
    u.add_argument("--metin", required=True)

    sub.add_parser("ruhsat")

    a = p.parse_args()
    if a.komut == "ruhsat":
        print(ruhsat_ac())
        return

    kontrol(a.metin)
    if a.komut == "sifrele":
        gizli = kaydir(a.metin, a.kat)
        puan, kelimeler = tehlike(a.metin)
        print(gizli)
        print(f"tehlike={puan} anahtarlar={kelimeler or ['yok']}")
    elif a.komut == "coz":
        print(kaydir(a.metin, a.kat, geri=True))
    else:
        puan, kelimeler = tehlike(a.metin)
        print(f"tehlike={puan} anahtarlar={kelimeler or ['yok']}")


if __name__ == "__main__":
    main()
