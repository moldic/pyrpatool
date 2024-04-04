import csv
import qrcode
import os

def main(dirname:str):

    with open(f'{dirname}/1.csv') as f:
        rdr=csv.reader(f)
        for line in rdr:
            url,name=line
            makeqr(url,f'{dirname}/{name}')



def makeqr(url,name):
    qr=qrcode.QRCode(
        version=1,
        error_correction=3,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True) 
    img=qr.make_image(fill_color="black",back_color="white")
    img.save(f'{name}.png')
    print(name)

if __name__=="__main__":
    # main(os.getcwd())
    main(os.path.dirname(__file__))
