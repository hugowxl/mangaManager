"""应用配置：漫画根目录等"""
import os
from pathlib import Path

# 漫画资源根目录，可通过环境变量 COMIC_ROOT 覆盖
DEFAULT_COMIC_ROOT = "D:\\comics"  # Windows 默认示例，请按实际修改
COMIC_ROOT = Path(os.environ.get("COMIC_ROOT", DEFAULT_COMIC_ROOT))

# 允许的图片扩展名
ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"}

# 服务配置
HOST = "0.0.0.0"  # 监听所有网卡，可通过本机 IP 访问
PORT = 8000
