# hotface

hotface是基于Flask开发的一个比较网站，灵感来自于[VSChart](http://vschart.com)。

demo: [hotface](http://blog.csdn.net/maliao1123)

[flask开发资源（包括git开源项目和相关书籍）](https://github.com/humiaozuzu/awesome-flask)

## 一、安装依赖（保证网站运行的相关库）

`
pip install -r requirement.txt
`


## 二、修改配置文件（保证在本地能够正确运行）
```
app/config.py
```

## 三、多种方式部署运行

`
gunicorn wsgi:app -c gunicorn.conf
`

or

`
python manage.py
`
