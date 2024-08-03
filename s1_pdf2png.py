from pdf2image import convert_from_path
from PIL import Image
import os
from tqdm import tqdm

def pdf_to_png(pdf_path, output_folder, start, end, dpi=600):

    start = int(start)
    end = int(end)

    if not os.path.exists(output_folder):
        print(f"創建 {output_folder} 資料夹")
        os.makedirs(output_folder)

    if start < 1 or start > end:
        print("頁碼範圍不正確")
        return

    print("讀取 PDF 文件中，請稍等…")
    images = convert_from_path(pdf_path, dpi=dpi, first_page=start, last_page=end)

    # 遍历图像并将它们保存为 PNG
    for i, image in tqdm(enumerate(images), desc="Converting PDF to PNG"):
        output_path = os.path.join(output_folder, f'{start + i}.png')
        image.save(output_path, 'PNG')

# 使用示例
pdf_path = input('請輸入 PDF 文件的名稱（放在同一个資料夾裡面/包含 .pdf）：') 
page_start = input("請輸入要切割的 PDF 對應到的起始页：")
page_end = input("請輸入要切割的 PDF 對應到的结束页：")
output_folder = input('請輸入輸入出的資料夾（例如：page_png）：')  
dpi = 600  

pdf_to_png(pdf_path, output_folder, page_start, page_end, dpi)
