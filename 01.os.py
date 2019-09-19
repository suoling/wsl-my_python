# w = open("myfile.txt", "w", encoding="utf-8")

# for i in range(10000):
#     w.write(str(i) + '药耀源是个变态\n')

# w.close()

# r = open("myfile.txt", "r", encoding="utf-8")

# # print(r.read(80))

# while tmp = r.readline(), tmp != '':
#     print(tmp)

# r.close()

with open("myfile.txt") as f:
  for line in f.readlines():
    print(line)