import qrcode
import argparse

def generate_qr(data, filename="qr.png", fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    print(f"二维码已保存到: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="简单 QR Code 生成器")
    parser.add_argument("text", help="要编码的文字或链接")
    parser.add_argument("--output", "-o", default="qr.png", help="输出文件名")
    parser.add_argument("--color", default="black", help="前景色 (默认 black)")
    parser.add_argument("--bg", default="white", help="背景色 (默认 white)")

    args = parser.parse_args()
    generate_qr(args.text, args.output, args.color, args.bg)