from rembg import remove
import os

src_dir = r"C:\Users\USER\OneDrive - LIVSMED Inc\바탕 화면"
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(out_dir, exist_ok=True)

files = [
    ("KakaoTalk_20260901_184637282.jpg", "artisential-box-full.png"),
    ("KakaoTalk_20260901_184637282_01.jpg", "artisential-box-open.png"),
    ("KakaoTalk_20260901_184637282_03.jpg", "artisential-box-label.png"),
]

for src_name, out_name in files:
    src_path = os.path.join(src_dir, src_name)
    with open(src_path, "rb") as f:
        input_data = f.read()
    output_data = remove(input_data)
    out_path = os.path.join(out_dir, out_name)
    with open(out_path, "wb") as f:
        f.write(output_data)
    print(out_name, len(output_data), "bytes")
