import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("This is new QR code")
qr.png("img1.png", scale=8)

d = decode(Image.open("img2.png"))
print(d[0].data.decode("ascii"))