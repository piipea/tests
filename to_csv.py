#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import csv

dict = {
    "192.168.0.1": {"categories": ["OPER", "OPER_CAT1", "OPER_CAT2"]},
    "192.168.0.2": {"categories": ["OPER", "OPER_CAT2"]},
    "192.168.0.3": {"categories": ["OPER", "OPER_CAT3"]},
}

dict2 = {
    "01": {"ip": "192.168.0.1", "host": "testhost1", "categories": ["CAT1", "CAT2"]},
    "02": {"ip": "192.168.0.2", "categories": ["CAT1", "CAT3"]},
    "03": {"ip": "192.168.0.3", "host": "testhost3", "categories": ["OPER", "CAT3"]},
}

# for key, value in dict.items():
#    print("{" + str(key) + ":" + str(value) + "}")

csv_lines = []

for item in dict2:
    csv_lines.append(dict2[item])

with open("res.csv", "w") as f:
    w = csv.DictWriter(f, fieldnames=["ip", "host", "categories"])
    w.writeheader()
    w.writerows(csv_lines)
