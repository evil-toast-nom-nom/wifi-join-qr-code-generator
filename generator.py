import qrcode
qr = qrcode.QRCode()

wifi_network_name = "my wifi name"
wifi_password = "my wifi password"
wifi_security = "WPA"

qr.add_data(f"WIFI:S:{wifi_network_name};T:{wifi_security};P:{wifi_password};;")
qr.make()
img = qr.make_image(fill_color="black", back_color="white")

img.save("wifi.jpg")
img.show()
