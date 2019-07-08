# 深交所爬虫（测试）

## 启动

运行命令

```shell
scrapy crawl apispider
````

指定日志

```shell
scrapy crawl apispider -s LOG_FILE=scrapy.log
```

## 代码编号

将代码编号保存到`codes.csv`，启动时读取。保存的格式

```
1001
1002
1003
1004
```

只需要第一列。
