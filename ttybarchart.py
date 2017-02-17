#!/usr/bin/python3

plot = '■'

import sys

data = ((len(sys.argv) > 1) and open(sys.argv[1]) or sys.stdin).readlines()
data = [item.strip().split('\t') for item in data]
data = [(str(label), int(value)) for (label, value) in data ]

labels, values = zip(*data)
max_label_width = max(map(lambda x: len(str(x)), labels))
del labels

max_value_width = max(map(lambda x: len(str(x)), values))
max_value = max(values)
del values

from shutil import get_terminal_size
terminal_width, terminal_height = get_terminal_size((80,25))
max_width = terminal_width - max_label_width - max_value_width - 2

for label, value in data:
	print(label.rjust(max_label_width), plot * int(max_width * value / max_value), value)
