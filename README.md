# meizhuo
爬取美桌网的明星图片
### 准备过程：

requests, xpath, re

### 分析过程：

我们打开美桌网随便进入一个明星的主页

这里我们以朱一龙为例  http://www.win4000.com/mt/zhuyilong.html：

![meizhuo](meizhuo.png)

可以看到，有很多组不同主题的图片库

![meizhuo1](meizhuo1.png)

进入每个图片库会还有几张图片

这里我们通过请求主题图库的url之后

再通过解析出下一张图片的url继续进行请求得到每一张图片的url

之后再通过请求每个url返回二进制形式保存图片

这里附上我爬到的图片（因为不是用多进程所以就爬了一页）

![meizhuo2](meizhuo2.png)
