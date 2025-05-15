import os
from PIL import Image
from pathlib import Path
from tqdm import tqdm
import time
import json
import random


def show_banner():
    banner = f'''\033[36m
\t╔═══════════════════════════════════════════╗
\t║      (｡･ω･｡)ﾉ♡ Nudeify 净化程序           ║
\t╚═══════════════════════════════════════════╝

\t    _   _           _      _  __       
\t   | \ | |_   _  __| | ___(_)/ _|_   _ 
\t   |  \| | | | |/ _` |/ _ \ | |_| | | |
\t   | |\  | |_| | (_| |  __/ |  _| |_| |
\t   |_| \_|\__,_|\__,_|\___|_|_|  \__, |
\t                                  |___/ 

\t╔═══════════════════════════════════════════╗
\t║   脱脱脱~快把小秘密交出来吧♥              ║
\t║   「我会温柔的......处理干净的」          ║
\t╚═══════════════════════════════════════════╝\033[0m
    '''
    print(banner)
    time.sleep(1.2)  # 没什么用，纯装的


BASE_DIR = Path(__file__).parent
BEFORE_DIR = BASE_DIR / 'sexret_girls'
AFTER_DIR = BASE_DIR / 'clean_slut'


def strip_exif(img_path: Path, output_path: Path):
    try:
        image = Image.open(img_path)
        data = list(image.getdata())
        image_no_exif = Image.new(image.mode, image.size)
        image_no_exif.putdata(data)
        image_no_exif.save(output_path)
        tqdm.write(f"  ✅\033[32m完成\033[0m: {img_path.name} \033[32m脱光光咯~\033[0m]")
    except Exception as e:
        tqdm.write(f"  ❌\033[31m失败\033[0m]: {img_path.name}, \033[31m原因\033[0m]: {e}\n")


def load_moan_lines() -> list:
    moan_file = Path(__file__).parent / 'moan_lines.json'
    if moan_file.exists():
        with open(moan_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def say_random_moan(lines: list):
    if lines:
        tqdm.write("\033[34m  💬 " + random.choice(lines) + "\033[0m\n")

def main():
    show_banner()
    moan_lines = load_moan_lines()

    image_files = [f for f in BEFORE_DIR.iterdir() if f.is_file() and f.suffix.lower() in ['.jpg', '.jpeg', '.png']]

    if not image_files:
        print("没有找到要脱衣服的女孩们呢......快放进去一些吧！")
        return

    print(f"发现 {len(image_files)} 张性感照片, 准备净化喽~\n")
    time.sleep(0.5)

    for file in tqdm(image_files, desc="净化进度", ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:3.0f}%]'):
        output_file = AFTER_DIR / file.name
        strip_exif(file, output_file)
        say_random_moan(moan_lines)

    print("\n(///>_<)ﾉ 全、全部都处理好了！你真是个坏蛋～")


if __name__ == '__main__':
    main()
