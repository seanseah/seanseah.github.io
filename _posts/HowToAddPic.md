添加来自图床的图片外链：

替换 ""(英文输入下的引号) 里的链接，也就是例子中的「http://xxx.jpg」为自己上传图片（一般只有在图床上传的图才有这样的链接）的外链。

<figure>
    <img src="http://xxx.jpg">
</figure> 
    
两张并排显示：

<figure class="half">
    <img src="http://xxx.jpg">
    <img src="http://yyy.jpg">
</figure>
    
三张并排显示：

<figure class="third">
    <img src="http://xxx.jpg">
    <img src="http://yyy.jpg">
    <img src="http://zzz.jpg">
</figure>

### 添加 Github 图片

替换「/images/xxx.jpg」这样的链接为自己放置图片的路径。

单张居中显示：

<figure>
    <img src="{{ site.url }}/images/xxx.jpg"></a>
</figure>

两张并排显示：

<figure class="half">
    <img src="{{ site.url }}/images/xxx.jpg">
    <img src="{{ site.url }}/images/yyy.jpg">
</figure>

三张并排显示：

<figure class="third">
    <img src="{{ site.url }}/images/xxx.jpg">
    <img src="{{ site.url }}/images/yyy.jpg">
    <img src="{{ site.url }}/images/zzz.jpg">
</figure>

### 附加浏览窗口的模式：

两张（Github 图片）并排显示：

<figure class="half">
    <a href="{{ site.url }}/images/xxx.jpg"><img src="{{ site.url }}/images/ xxx.jpg"></a>
    <a href="{{ site.url }}/images/yyy.jpg"><img src="{{ site.url }}/images/ yyy.jpg"></a>
</figure>

so on