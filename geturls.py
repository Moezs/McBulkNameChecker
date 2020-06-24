import requests
import logging

i = 0
f = open("names.txt", 'r')

file = open("names.txt", "r")

number_of_lines = 0

for line in file:
  line = line.strip("\n")

  words = line.split()
  number_of_lines += 1
file.close()

for i in range(number_of_lines):
  line = f.readline()
  line = line.strip()
  url = "https://api.mojang.com/users/profiles/minecraft/"+line
  logging.basicConfig(format='%(message)s',filename="urls.txt", level=logging.DEBUG)
  
  logging.debug(url)


raw_input()
