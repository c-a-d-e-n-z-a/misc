import os
from markitdown import MarkItDown

def convert_directory(input_dir, output_dir, md):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(input_dir):
        relative_path = os.path.relpath(root, input_dir)  # 計算相對路徑
        output_subdir = os.path.join(output_dir, relative_path)  # 建立對應的輸出目錄

        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        for file in files:
            if file.endswith(".html") or file.endswith(".htm") or file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".doc"):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_subdir, os.path.splitext(file)[0] + ".md")

                result = md.convert(input_path)

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result.text_content)

                print(f"Converted: {input_path} -> {output_path}")



md = MarkItDown()


# 設定輸入目錄和輸出目錄
input_directory = r'd:\PERSONAL\FINANCE\INVESTMENT\\'
output_directory = r'r:\MD\\'

convert_directory(input_directory, output_directory, md)