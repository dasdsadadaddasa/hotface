HOTFACE

HOTFACE是基于Flask开发的一个比较网站，灵感来自于VSChart。

demo: HOTFACE

flask开发全资源
安装依赖

pip install -r requirement.txt
配置文件

app/config.py

运行

gunicorn wsgi:app -c gunicorn.conf

or

python manage.py
