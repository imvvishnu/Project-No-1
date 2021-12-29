import pyqrcode
url = "https://www.bing.com/videos/search?q=god+of+war+5+trailer&docid=608028882389049535&mid=6DAFF647CB3B18B965AC6DAFF647CB3B18B965AC&view=detail&FORM=VIRE"
k = pyqrcode.create(url)
k.svg('Qr.svg' , scale = 10)
