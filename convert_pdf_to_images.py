from pdf2image import convert_from_path
pages = convert_from_path('data/FB/fb-20211231.pdf', 500)

for page in pages:
    print(page)
    exit()
    # page.save('out.jpg', 'JPEG')
