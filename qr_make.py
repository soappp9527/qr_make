import pandas as pd
import qrcode
from PIL import Image, ImageDraw, ImageFont

data = pd.read_csv("资产表.csv", encoding = "gb2312")
#data.head()

def qrmake(df):
  qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
    )
    
  qr.add_data("资产编号: {}\n \
               设备名称: {}\n \
               型号&规格: {}\n \
               品牌: {}\n \
               所属单位: {}\n \
               放置地点: {}\n \
               购买日期: {}\n"
               .format(df["资产编号"],
                       df["设备名称"],
                       df["型号&规格"],
                       df["品牌"],
                       df["单位"],
                       df["放置地点"],
                       df["购买日期"]
                       ))
                       
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  #font = ImageFont.truetype("msyh.ttc", 50, encoding="utf-8")
  #t = ImageDraw.Draw(img)
  #label = "高品医学检验财产标签"
  #label = label.encode("utf-8").decode("latin1")
  #t.text((12,12), text = label)
  img.save("{}.jpg".format(df["资产编号"]))
  


data.apply(qrmake, axis=1)

