import qrcode

data = "https://pooja9293.github.io/Portfolio/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("qrcode.png")
qr_img.show()
