import os
from heic2png import HEIC2PNG
from tqdm import tqdm

if __name__=="__main__":
    dir_name = ""
    outpur_dir = ""

    ext = (".HEIC", ".HEIF")
    heic_files = [f for f in os.listdir(dir_name) if f.endswith(ext)]

    with tdqm(total=len(heic_files), desc="Converting images", unit="file") as pbar:
        for files in os.listdir(dir_name):
            if files.endswith(ext):
                try:
                    img = HEIC2PNG(f"{dir_name}\\{files}", quality=100)
                    files = files[:-5]
                    img.save(f"{output_dir}\\{files}.png")
                    pbar.update(1)

                except FileExistsError:
                    pbar.update(1)
                    continue

            else:
                continue
