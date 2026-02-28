"""API 层：漫画相关 HTTP 接口"""
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse

from service.comic_service import ComicService

router = APIRouter(prefix="/api", tags=["comic"])
_service = ComicService()


@router.get("/comics", response_class=JSONResponse)
def list_comics():
    """获取所有漫画列表"""
    return _service.list_comics()


@router.get("/comics/{comic_id}", response_class=JSONResponse)
def get_comic(comic_id: str):
    """获取单本漫画信息"""
    comic = _service.get_comic(comic_id)
    if not comic:
        raise HTTPException(status_code=404, detail="漫画不存在")
    return comic


@router.get("/comics/{comic_id}/pages", response_class=JSONResponse)
def list_pages(comic_id: str):
    """获取某本漫画的页面列表"""
    comic = _service.get_comic(comic_id)
    if not comic:
        raise HTTPException(status_code=404, detail="漫画不存在")
    return _service.list_pages(comic_id)


@router.get("/comics/{comic_id}/pages/{filename:path}")
def get_page_image(comic_id: str, filename: str):
    """获取漫画某一页的图片文件（流式返回）"""
    path = _service.get_page_path(comic_id, filename)
    if not path or not path.exists():
        raise HTTPException(status_code=404, detail="页面不存在")
    return FileResponse(path, media_type=None)
