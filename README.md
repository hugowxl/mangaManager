# 漫画管理系统

基于 Python FastAPI 的后端项目，采用 **API 层 / Service 层 / DAO 层** 结构，用于在浏览器中浏览指定硬盘目录下的漫画资源。

## 项目结构

```
├── api/              # API 层：HTTP 路由
│   └── comic_api.py
├── service/          # Service 层：业务逻辑
│   └── comic_service.py
├── dao/              # DAO 层：数据/文件访问
│   └── comic_dao.py
├── config/           # 配置
│   └── settings.py
├── templates/        # 网页模板
│   ├── index.html    # 漫画列表页
│   └── reader.html   # 阅读器页
├── main.py           # 应用入口
└── requirements.txt
```

## 漫画目录约定

- 在配置中指定一个**漫画根目录**（如 `D:\comics`）。
- 根目录下的**每个子文件夹**视为一本漫画，文件夹名即漫画标题。
- 每本漫画文件夹内放图片文件（如 `.jpg`、`.png`），按文件名排序后即为阅读顺序。

示例：

```
D:\comics\
├── 漫画A\
│   ├── 001.jpg
│   ├── 002.jpg
│   └── ...
└── 漫画B\
    ├── 01.png
    └── 02.png
```

## 配置

在 `config/settings.py` 中修改默认漫画根目录：

```python
DEFAULT_COMIC_ROOT = "D:\\comics"  # 改成你的实际路径
```

或通过环境变量（无需改代码）：

```powershell
$env:COMIC_ROOT = "E:\manga"
python main.py
```

## 安装与运行

在项目根目录下执行：

```powershell
cd d:\porject
pip install -r requirements.txt
python main.py
```

启动后会打印本机 IP 和端口，例如：

- 本机访问：http://127.0.0.1:8000  
- 局域网访问：http://你的IP:8000  

在浏览器打开上述地址即可进入漫画列表页，点击某本漫画进入阅读器。

## API 说明

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/comics` | 获取所有漫画列表 |
| GET | `/api/comics/{comic_id}` | 获取单本漫画信息 |
| GET | `/api/comics/{comic_id}/pages` | 获取该漫画的页面列表 |
| GET | `/api/comics/{comic_id}/pages/{filename}` | 获取某一页图片 |

接口文档（运行后访问）：http://127.0.0.1:8000/docs  

## 技术栈

- **FastAPI**：Web 框架
- **Uvicorn**：ASGI 服务器
- **Jinja2**：HTML 模板
