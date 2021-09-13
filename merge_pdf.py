# GAMMASOFT pytyonでフォルダ内のPDFファイルを１つにまとめる
# 
# PyPDF2のインストール
# > python -m pip install pypdf2

from pathlib import Path
import PyPDF2

# フォルダ内のPDFファイル一覧
pdf_dir = Path('./pdf_files')
pdf_files = sorted(pdf_dir.glob('*.pdf'))

# 1つのPDFファイルにまとめる
pdf_writer = PyPDF2.PdfFileWriter()
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i))
# 保存ファイル名(先頭と末尾のファイル名で作成)
merged_file = pdf_files[0].stem + "-" + pdf_files[-1].stem + ".pdf"

# 保存
with open(merged_file, "wb") as f:
    pdf_writer.write(f)

'''
  ├ pdf_files/
  │  ├ 201901hyoshi.pdf
  │  ├ 201902hyoshi.pdf
  │  ├ 201903hyoshi.pdf
  │  └ 201903nankai_gaikyo.pdf
  │
  ├ 201901hyoshi-201903nankai_gaikyo.pdf
  └ merge_pdf.py
'''