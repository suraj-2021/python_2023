import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=10,border=4,)

qr.add_data("https://www.jaipurdialoues.com")
qr.make(fit=True)
img.save("wscube_web.png")
