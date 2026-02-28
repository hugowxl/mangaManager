"""漫画管理系统入口：启动后可通过本机 IP:8000 访问"""
import socket
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape

from api.comic_api import router as comic_router
from config.settings import COMIC_ROOT, HOST, PORT

app = FastAPI(title="漫画管理系统", description="API + 网页浏览指定目录下的漫画资源")
app.include_router(comic_router)

# 前端模板目录
TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
env = Environment(
    loader=FileSystemLoader(str(TEMPLATES_DIR)),
    autoescape=select_autoescape(["html", "xml"]),
)


def get_local_ip() -> str:
    """获取本机局域网 IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """首页：漫画列表与阅读入口"""
    template = env.get_template("index.html")
    base_url = str(request.base_url).rstrip("/")
    return template.render(
        base_url=base_url,
        comic_root=str(COMIC_ROOT),
    )


@app.get("/reader/{comic_id}", response_class=HTMLResponse)
async def reader(request: Request, comic_id: str):
    """阅读器页面：按页查看漫画"""
    template = env.get_template("reader.html")
    base_url = str(request.base_url).rstrip("/")
    return template.render(
        base_url=base_url,
        comic_id=comic_id,
    )


if __name__ == "__main__":
    import uvicorn

    local_ip = get_local_ip()
    print(f"漫画根目录: {COMIC_ROOT}")
    print(f"请确保该目录存在且包含子文件夹（每个子文件夹为一本漫画）")
    print(f"本机访问: http://127.0.0.1:{PORT}")
    print(f"局域网访问: http://{local_ip}:{PORT}")
    uvicorn.run(app, host=HOST, port=PORT)
