![bars.jpg](https://i.loli.net/2018/07/30/5b5ebbb4da73a.jpg)

# Spencer's Simple-Desktop-API | 一喵一图

![love](https://img.shields.io/badge/Made%20with-LOVE-ff69b4.svg)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![README](https://img.shields.io/badge/Readme-English-orange.svg)](https://github.com/spencerwoo98/spencer-simple-desktop-api/blob/master/README.md)

一个异常简单的随机图片 API，图源自极简主义桌面壁纸提供网站 → [Simple Desktops](http://simpledesktops.com) 🎉🎉🎉

## Simple Desktops? 这是什么？

Simple Desktops 提供了...

> A collection of wallpapers designed to make your computer beautiful without distraction.

一组特别设计的壁纸，让你电脑桌面美观的同时又不妖艳而令人分心。

我个人十分喜欢 Simple Desktops 提供的壁纸，它们简单、清晰，又符合设计美学。因此我也很想将 Simple Desktops 上面的壁纸用作我博客题图、文章配图等等地方。我于是设计了这样一个 API，它能够十分方便的将 Simple Desktops 的图片直接嵌入任何地方。

## 使用方法

直接将下面代码嵌入你想要放的地方。不必担心是否支持 `https`，因为不仅 `API` 的 `GET` 请求是通过 `https` 传输的，图片本身也是通过 `https` 传输的。( •̀ ω •́ )y

**1. API 地址**

```html
https://api.spencerwoo.com
```

**2. Markdown**

```html
![img](https://api.spencerwoo.com)
```

**3. HTML**

```html
<img src="https://api.spencerwoo.com" alt="img.png" title="img.png" />
```

图片随机显示并且每次刷新都将更新新的图片。由于版权问题以及 Simple Desktops 本身并没有将图片进行分类，我自然无法将图片分类，同时由于 Simple Desktops 网站本身不支持 `https`，我无法也无益直接提供 Simple Desktops 的图片外链。

## 好看吗?

![sshot-1.png](https://i.loli.net/2018/07/30/5b5ecdb7b783a.png)

目前在使用 **「一喵一图」** 的网站有这些:

- https://spencerwoo.com
- https://chungzh.cn

如果你在使用我的 API 并且想将你的网站加到列表里面来，请直接 fork 项目，修改这里的列表，然后发一个 PR 就 ok 了。干杯。🎉

## 贡献

```
.
├── README.md
├── api.php
├── assets
│   ├── archlogo.png
│   └── imageToBeUploadedToSmms.png
├── index.php
├── simple-desktops.py
└── simple-desktops.txt

1 directory, 7 files
```

`simple-desktops.py` 将 Simple Desktops 的图片爬下来。图片下载至  `assets/imageToBeUploadedToSmms.png` 然后上传至 SM.MS 图床。图片返回外链地址储存在 `simple-desktops.txt`.

如果你想在自己的服务器上面搭建这个服务，将上述代码直接放到服务器的 `nginx` 根目录，重启 `nginx` 服务，然后去 `$你的服务器 IP$/api` 就可以看到啦。🎊

欢迎 Star，欢迎 PR。

## 致谢与版权声明

**服务稳定全靠天，随时跑路不留名。**

- Images at Simple Desktops are for personal use and for personal use only. They shouldn't be sold or reposted without the expressed written consent of the desktop creator. See [Simple Desktops](http://simpledesktops.com/about/) for more details.
- A huge thank you to SM.MS for providing such a stable and awesome image hosting service. 
- Server provided by [VULTR - The Infrastructure Cloud™](https://www.vultr.com/).
 
项目经由 MIT License 发布。

[© Spencer Woo](https://spencerwoo.com)
