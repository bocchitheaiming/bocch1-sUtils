import subprocess
import os

def crop_all_pdfs(current_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(current_dir):
        print(file)
        if file.lower().endswith(".pdf"):
            input_file = os.path.join(current_dir, file)
            output_file = os.path.join(output_dir, file)
            print(f"裁剪：{file}")
            try:
                subprocess.run(["pdfcrop", input_file, output_file], check=True, stdout=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                print(f"裁剪失败：{file}，请检查 pdfcrop 是否安装并在环境变量中。")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "cropped_pdf")
    crop_all_pdfs(current_dir, output_dir)
    print("全部裁剪完成！")