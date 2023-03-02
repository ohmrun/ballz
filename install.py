import os
with open("repos") as file:
    for line in file:
      arr = line.rstrip().split()
      l = arr[0]
      r = arr[1]
      os.system(f'haxelib run gsm add {l} {r}')
