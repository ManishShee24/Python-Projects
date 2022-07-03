import qrcode

code_f = qrcode.QRCode(box_size = 35, border = 3)
code_f.add_data('https://github.com/ManishShee24/Python-Projects')
code_f.make(fit = True)

qrcode_img = code_f.make_image(fill_color = 'black', back_color = 'white')
qrcode_img.save('qrcode_img.png')
