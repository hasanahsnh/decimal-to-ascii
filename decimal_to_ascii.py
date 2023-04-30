decimal_list = input('masukkan list angka decimal (pisahkan dengan koma): ')
decimal_list = [int(decimal) for decimal in decimal_list.split(',')]
ascii_string = ''.join([chr(decimal) for decimal in decimal_list])
print(ascii_string)
