#!/usr/bin/env python3

nomes = ("Denis", "Ingrid", "Livia", "Cacau")

nomes_list = [familia.upper() for familia in nomes if familia.startswith("D") ]

print(nomes_list)