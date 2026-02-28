"""DAO 层：漫画与页面的文件系统访问"""
from pathlib import Path
from typing import List, Optional

from config.settings import COMIC_ROOT, ALLOWED_IMAGE_EXTENSIONS


class ComicDao:
    """漫画数据访问：扫描目录、读取页面列表"""

    def __init__(self, root: Optional[Path] = None):
        self.root = root or COMIC_ROOT

    def get_comic_root(self) -> Path:
        return self.root

    def list_comics(self) -> List[dict]:
        """列出根目录下所有漫画（每个子目录视为一本漫画），含第一页作为封面"""
        if not self.root.exists() or not self.root.is_dir():
            return []
        result = []
        for item in sorted(self.root.iterdir()):
            if item.is_dir() and not item.name.startswith("."):
                pages = self.list_pages(item.name)
                cover_filename = pages[0]["filename"] if pages else None
                result.append({
                    "id": item.name,
                    "title": item.name,
                    "path": str(item),
                    "cover_filename": cover_filename,
                })
        return result

    def get_comic_by_id(self, comic_id: str) -> Optional[dict]:
        """根据 id（目录名）获取单本漫画信息"""
        path = self.root / comic_id
        if not path.exists() or not path.is_dir():
            return None
        return {
            "id": comic_id,
            "title": comic_id,
            "path": str(path),
        }

    def list_pages(self, comic_id: str) -> List[dict]:
        """列出某本漫画下的所有页面（图片文件），按文件名排序"""
        path = self.root / comic_id
        if not path.exists() or not path.is_dir():
            return []
        pages = []
        for f in sorted(path.iterdir(), key=lambda x: x.name.lower()):
            if f.is_file() and f.suffix.lower() in ALLOWED_IMAGE_EXTENSIONS:
                pages.append({
                    "filename": f.name,
                    "index": len(pages),
                })
        return pages

    def get_page_path(self, comic_id: str, filename: str) -> Optional[Path]:
        """获取某一页的完整路径，用于安全地读取文件"""
        path = self.root / comic_id / filename
        if not path.exists() or not path.is_file():
            return None
        # 防止路径穿越：确保 path 在 comic 目录内
        try:
            path.resolve().relative_to((self.root / comic_id).resolve())
        except ValueError:
            return None
        if path.suffix.lower() not in ALLOWED_IMAGE_EXTENSIONS:
            return None
        return path
