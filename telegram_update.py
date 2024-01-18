import time
import sys
import contextlib
from httpx import get, post

token = str(sys.argv[1])
frontend = str(sys.argv[2])
backend = str(sys.argv[3])

text = (f"#更新日志 #Sub-store 前端+后端 本地化部署\n"
        f"🔨前端版本：{frontend}，后端版本：{backend}\n"
        "本仓库地址：https://api.github.com/repos/chenyk1219/Sub-Store-Local\n"
        "源码仓库地址：https://github.com/sub-store-org/")

url = f"https://api.telegram.org/bot{token}/sendMessage"
for cid in ["-1002083747718"]:
    push_content = {
        "chat_id": cid,
        "disable_web_page_preview": "True",
        "parse_mode": "markdown",
        "text": text,
    }
    with contextlib.suppress(Exception):
        main_req = post(url, data=push_content)
    time.sleep(1)
