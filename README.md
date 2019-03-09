# tldr_cn

## 缘起
you know tldr, this script make the tips tanslated to chinese simple
i don't know, just for test

## 此物
一个Python脚本，先用request请求tldr， 然后发现原文就是Markdown语法的文本
然后用Python的googletrans 库进行Google翻译， 把tldr里面的说明文字翻译成中文
本来以为还要用正则提取文本的， 结果发现在进行谷歌翻译的时候，会自动忽略`cd `这样的格式，
也就是说不用正则就行了， 直接把原文放到谷歌翻译里就行了，那真是太棒了

正则表达式也太难了啊。。。。。。。。用起来完全懵逼的感觉

## 如何
`python3 tldr_cn.py cd`
