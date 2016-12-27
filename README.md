# hotface

hotface是基于Flask开发的一个比较网站，灵感来自于[VSChart](http://vschart.com)。

demo: [hotface](http://blog.csdn.net/maliao1123)

[flask开发资源（包括git开源项目和相关书籍）](http://blog.csdn.net/maliao1123)

## 安装依赖

`
pip install -r requirement.txt
`


## 配置文件

```
app/config.py
```

## 运行

`
gunicorn wsgi:app -c gunicorn.conf
`

or

`
python manage.py
`
