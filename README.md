![bars.jpg](https://i.loli.net/2018/07/30/5b5ebbb4da73a.jpg)

# Spencer Image API for Simple Desktops

![love](https://img.shields.io/badge/Made%20with-LOVE-ff69b4.svg)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A dead simple random image API for web pages. Images curated by the magnificent ones at Simple Desktops. 🎉🎉🎉

## What is Simple Desktops?

Simple Desktops is ...

> A collection of wallpapers designed to make your computer beautiful without distraction.

Personally, I really like the design and simplicity of the images Simple Desktops provide. So I really wanted to put those on my blog, or other web pages. So I whipped up this API to randomize an image that I can easily embed in my blog posts.

## Usage

Embed the following code into your desired places. Don't worry about `https` support, all redirected image links are served over `https`. 🐱‍👤

**1. Plain URL**

```html
http://api.spencerwoo.com
```

**2. Markdown**

```html
![img](http://api.spencerwoo.com)
```

**3. HTML**

```html
<img src="http://api.spencerwoo.com" alt="img.png" title="img.png" />
```

Images are reloaded and randomized with every refresh.

## Contributing

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

`simple-desktops.py` is for scraping down images at Simple Desktops. Images are downloaded to `assets/imageToBeUploadedToSmms.png` and then uploaded to SM.MS image hosting service. The response image url is stored at `simple-desktops.txt`.

If you consider serving this at your own server, put all files above at your server's web root. Then go for `$YourServerIP/api$` and see that in action. 🎊

Contributions are welcome.

Websites using `Spencer Image API for Simple Desktops`:

- https://spencerwoo.com

If you are using my API and wish to be added to the list, fork the project, add yourself to the list here, and make a PR. Cheers. 🎉

## Acknowledgements

- Images at Simple Desktops are for personal use and for personal use only. They shouldn't be sold or reposted without the expressed written consent of the desktop creator. See [Simple Desktops](http://simpledesktops.com/about/) for more details.
- A huge thank you to SM.MS for providing such a stable and awesome image hosting service. 
- Server provided by [VULTR - The Infrastructure Cloud™](https://www.vultr.com/)
 
This project is published under the MIT License. 

© Spencer Woo