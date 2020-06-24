import requests
i = 0
f = open("urls.txt", 'r')

file = open("urls.txt", "r")

number_of_lines = 0

for line in file:
  line = line.strip("\n")

  words = line.split()
  number_of_lines += 1
file.close()

for i in range(number_of_lines):
  line = f.readline()
  line = line.strip()
  print(line)
  r = requests.get(line)
  if r.status_code == 200:
    print("taken")
  else:
    print("available")


raw_input()
