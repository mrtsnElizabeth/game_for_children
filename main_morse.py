#!python3
lines = open('morse.txt').read().splitlines()
decode_dict = {}
encode_dict = {}
for line in lines:
  pair = line.split()
  letter = pair[0]
  morse = pair[1]
  decode_dict[morse] = letter
  encode_dict[letter] = morse

mode = input("Выберите режим: 1=Кодирование, 2=Декодирование")
file_name = input("Введите имя файла: ")
if mode == "2":
  message = open(file_name).read().splitlines()
  decoded = ""
  for code in message:
    if code in decode_dict:
      letter = decode_dict[code]
      decoded = decoded + letter
    elif code == '':
      decoded += " "
    else:
      decoded += "?"
      print("Неизвестный код", code)
  print(decoded)
elif mode == "1":
  message = open(file_name).read()
  encoded = ""
  for code in message:
    if code in encode_dict:
      letter = encode_dict[code]
      encoded = encoded + letter
    elif code == ' ':
      encoded += " "
    else:
      encoded += "?"
      print("Неизвестный код", code)
  print(encoded)
else:
  print("Неподдерживаемый режим ", mode)
