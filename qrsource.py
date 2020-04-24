import qrcode
"""
ここをもとに勉強してく＾～
https://note.nkmk.me/python-pillow-qrcode/
"""
## making QR module
ID = int(input("QRに盛り込むintデータを入力："))
img = qrcode.make(ID)
print(type(img))
print(img.size)
link = "./" + str(ID) + "_qr.png" 
img.save(link)

## decoding QR module
