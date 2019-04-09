<div align="center">

<img src="assets/Bannero.png" width="80%">
<h1> Bannero API </h1>
<p>🚀🥇🗳</p>

<strong><p> Simple random banner pictures for blogs, websites and more.</p></strong>

[![](https://img.shields.io/badge/Deployed%20to-HEROKU-%237B5CA3.svg?logo=heroku&style=for-the-badge)](https://bannero.herokuapp.com/)
![GitHub](https://img.shields.io/github/license/spencerwooo/bannero.svg?style=for-the-badge)

</div>

**I'm BACK!**

## What is Simple Desktops?

Simple Desktops is ...

> A collection of wallpapers designed to make your computer beautiful without distraction.

Personally, I really like the design and simplicity of the images Simple Desktops provide. So I really wanted to put those on my blog, or other web pages. So I whipped up this API to randomize an image that I can easily embed in my blog posts.

## Usage

Embed the following code into your desired places. Don't worry about `https` support, API's `GET` method is served over `https`, and all redirected image links are served over `https` too. 🐱‍👤

**1. Plain URL**

```html
https://bannero.herokuapp.com
```

**2. Markdown**

```html
![img](https://bannero.herokuapp.com)
```

**3. HTML**

```html
<img src="https://bannero.herokuapp.com" alt="img.png" title="img.png" />
```

Images are reloaded and randomized with every refresh.

## Does it look nice?

Of course.

![sshot-1.png](https://i.loli.net/2018/07/30/5b5ecdb7b783a.png)

Contributions are welcome.

## Building

- Install Python 3
- Install `pipenv`, then run:

```bash
pipenv install
```

- Go into Python virtual environment:

```bash
pipenv shell
```

- Run server at `localhost:9000`

```bash
python src/api.py
```

## Acknowledgements

- Images at Simple Desktops are for personal use and for personal use only. They shouldn't be sold or reposted without the expressed written consent of the desktop creator. See [Simple Desktops](http://simpledesktops.com/about/) for more details.
- A huge thank you to SM.MS for providing such a stable and awesome image hosting service.
- **App is proudly served at Heroku.**

---

**🚀 Bannero API** ©Spencer Woo. Released under the MIT License.

Created, authored and maintained by Spencer Woo.

[@Blog](https://spencerwoo.com/) · [ⒿJike](https://web.okjike.com/user/4DDA0425-FB41-4188-89E4-952CA15E3C5E/post) · [@GitHub](https://github.com/spencerwooo)
