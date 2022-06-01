import qrcode

qr = qrcode.QRCode(
    version=2, error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15, border=5
)
add_Link = input("Enter The Link For Which You Want To Get QR Code:\n")
qr.add_data(add_Link)
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
file_Name = input("Enter The File Name You Want To Save: \n")
img.save(file_Name + '.png')
