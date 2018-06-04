#!/usr/bin/env python3

import json


def write_out(payload):
    file_name = 'data.txt'
    with open(file_name, 'w') as f:
        json.dump(payload, f, ensure_ascii=False)

