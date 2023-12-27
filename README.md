# py-selenium-metamask
平时撸毛有很多小号，偶尔需要在浏览器手动操作，这个脚本可以帮忙批量导入metamask，进行一些简单的重复操作。代码其实比较简单，就是环境准备比较麻烦，selenium操作一般就是定位元素，输入数据，点击按钮

# 环境准备
## 我的环境是python3.9 selenium 4.16.0

selenium 4的语法和之前3差别很多，注意版本

## 根据自己chrome版本去官网下载相应的驱动chromedriver

https://chromedriver.storage.googleapis.com/index.html

https://chromedriver.chromium.org/downloads

https://googlechromelabs.github.io/chrome-for-testing/#stable


## 一般chrome多用户的用户资料在这里

C:\Users\自己的用户名\AppData\Local\Google\Chrome\User Data

最好自己复制一份，方便调试

C:\Users\自己的用户名\AppData\Local\Google\Chrome\User Data1

## 在chrome的快捷方式，右键，在属性这里修改如下，主要是添加了user-data-dir和remote-debugging-port这2个属性，方便直接调试

"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 10"  --user-data-dir="C:\Users\自己的用户名\AppData\Local\Google\Chrome\User Data1"   --remote-debugging-port=9222

# 运行脚本
## 安装selenium

pip install selenium

python py-selenium-metamask.py

# 元素的定位
## 最简单的就是xpath, F12, ctrl+shift+c选择元素，右键copy---copy XPath

browser.find_element(By.XPATH,'')
