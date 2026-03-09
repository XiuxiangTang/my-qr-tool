# my-qr-tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/XiuxiangTang/my-qr-tool?style=social)](https://github.com/XiuxiangTang/my-qr-tool)

一个轻量、纯命令行的 QR Code 生成工具。用 Python 实现，支持自定义颜色、输出 PNG 图片。适合脚本自动化、快速分享链接/文本等场景。

## 特性
- 一行命令生成二维码
- 支持任意前景色/背景色（HEX 或颜色名）
- 错误纠正级别可调（未来扩展）
- 无需 GUI，纯 CLI，易集成

## 安装（开发/测试用）
```bash
git clone https://github.com/XiuxiangTang/my-qr-tool.git
cd my-qr-tool
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install qrcode[pil]
python main.py "https://github.com" --output qr.png
