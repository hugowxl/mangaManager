"""Service 层：漫画业务逻辑"""
from pathlib import Path
from typing import List, Optional

from dao.comic_dao import ComicDao


class ComicService:
    """漫画业务：对外提供漫画列表、详情、页面列表等"""

    def __init__(self):
        self._dao = ComicDao()

    def list_comics(self) -> List[dict]:
        return self._dao.list_comics()

    def get_comic(self, comic_id: str) -> Optional[dict]:
        return self._dao.get_comic_by_id(comic_id)

    def list_pages(self, comic_id: str) -> List[dict]:
        return self._dao.list_pages(comic_id)

    def get_page_path(self, comic_id: str, filename: str) -> Optional[Path]:
        return self._dao.get_page_path(comic_id, filename)

    def get_comic_root(self) -> Path:
        return self._dao.get_comic_root()
