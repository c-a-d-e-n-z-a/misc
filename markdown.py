import os
from markitdown import MarkItDown

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def convert_directory(input_dir, output_dir, md):
    # Create all directories upfront
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Create output directory structure
    for root, _, _ in os.walk(input_dir):
        relative = Path(root).relative_to(input_path)
        (output_path / relative).mkdir(parents=True, exist_ok=True)

    # Supported file extensions
    supported_ext = {'.html', '.htm', '.pdf', '.docx', '.doc'}
    
    # Collect all files to process
    files_to_convert = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if Path(file).suffix.lower() in supported_ext:
                input_file = Path(root) / file
                output_file = (output_path / Path(root).relative_to(input_path) / 
                             file).with_suffix('.md')
                files_to_convert.append((input_file, output_file))

    # Process files in parallel
    def convert_file(input_file, output_file):
        result = md.convert(str(input_file))
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
        print(f"Converted: {input_file} -> {output_file}")

    with ThreadPoolExecutor() as executor:
        executor.map(lambda args: convert_file(*args), files_to_convert)



md = MarkItDown()


# 設定輸入目錄和輸出目錄
input_directory = r'd:\PERSONAL\FINANCE\INVESTMENT\\'
output_directory = r'r:\MD\\'

convert_directory(input_directory, output_directory, md)
