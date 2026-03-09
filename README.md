# my-qr-tool

一个超级简单的命令行 QR Code 生成工具，用 Python 写成。  
支持输入任意文字/链接，生成 PNG 图片，还能自定义前景色和背景色。

## 特性
- 快速生成二维码（CLI 一条命令搞定）
- 支持自定义颜色（前景/背景）
- 轻量级，只依赖 qrcode 和 Pillow

## 安装（本地开发/测试用）
```bash
git clone https://github.com/XiuxiangTang/my-qr-tool.git
cd my-qr-tool
python -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
python main.py "https://github.com" --output qr.png
# 基本用法
python main.py "你好，世界！" --output hello.png

# 彩色版本
python main.py "扫我领红包" --output hongbao.png --color red --bg yellow

# 链接示例
python main.py "https://x.com" -o x-qr.png --color "#0000FF" --bg white
