# visual-control-data
在平时场地操作手远程控制机器人的时候，想查看机器人内部数据，这种方法可以及其方便使数据显示在网站上，用手机或电脑输入链接即可实时查看。

#### 此项目是我用chatgpt辅助编写的，不得不说chatgpt真是程序员的神器。接下来我将分三部介绍此项目：作用，使用方法，代码解释。

### 1.作用
在我平常调机器人的时候，如果我想实时查看机器人的内部数据变化，那我只能进行debug，这样就相当于暂停机器人了，这样很不好，不方便。所以我基于此问题，我把机器人主机里的数据通过网络传到网页上，网页可以自己设计得符合各自的需求，我的项目把网页分为左右两部分，左边显示数据，右边显示机器人摄像头的图像。
### 2.使用方法
机器人主机要和您的可视化客户端处于一个局域网内，运行main.py,网页查看输入：http://127.0.0.1:5000（只能本地查看）或者：http://(本地ip地址):5000（可以其他主机查看）。
在手机查看时，建议设计网页全屏和手机设置自动旋转，这样观看效果更佳，这样方便把手机固定到手柄上方便操作手查看。
##### 电脑端：
![2023-02-11 10-20-50 的屏幕截图](https://user-images.githubusercontent.com/104723484/218234108-93389829-9489-40f4-b4ef-2c72213b7866.png)
##### 手机端：
![default](https://user-images.githubusercontent.com/104723484/218234501-61a288d4-a9b5-474c-a5e3-bd88cb5dd94f.jpg)
### 3.代码解释
本来我是懒得解释代码的，因为我在代码里面已经写了充分的注释，然后我发现我和chatgpt聊天时的一些解释也挺详细的，就顺便复制过来了！
#### gpt：
##### 如果您想在网页上实时显示数据，可以使用 JavaScript 和 Ajax 实现，将数据通过 API 接口实时传递到前端。

##### index.html里的代码实现了通过 JavaScript 和 Ajax 实现实时显示数字的功能。

##### 主要用到了以下几个 JavaScript 的 API：

##### XMLHttpRequest: 这是一个构建 HTTP 请求的 API，它允许前端通过 JavaScript 向后端发送 HTTP 请求。

##### setInterval: 这是一个 JavaScript 内置函数，它指定每隔一段时间执行一次某个函数。

##### 下面是详细的代码解释：

##### function updateNumber()：这是一个函数，它使用 XMLHttpRequest 向后端发送一个 GET 请求，并获取数据。

##### const xhr = new XMLHttpRequest()：这行代码创建了一个新的 XMLHttpRequest 对象，用于发送 HTTP 请求。

##### xhr.open("GET", "/api/data")：这行代码打开了一个 GET 请求，目标 URL 为/api/data，该 URL 映射到 Flask 应用中的/api/data路由。

##### xhr.onload = function()：这行代码指定了一个回调函数，当 HTTP 请求完成后会执行该函数。

##### const response = JSON.parse(xhr.responseText)：这行代码解析了 HTTP 请求返回的 JSON 响应，并将其转换为 JavaScript 对象。

##### setInterval(updateRandomNumber, 100)：这行代码指定了每隔100毫秒秒执行一次 `updateNumber

##### document.querySelector("#number1").innerText = response.numbers[0] 是 JavaScript 代码，它的作用是把获取的数据显示在网页上。

##### 它使用了 JavaScript 的 document.querySelector 函数，该函数可以通过选择器查找页面中的元素。

##### 在这里，选择器是 #number1，它代表的是带有 id 属性为 number1 的元素，在这个例子中，这个元素是一个<h>标签。

##### 接下来，通过使用 innerText 属性，可以设置元素中显示的文本内容。在这里，它被设置为从服务器端返回的数据列表的第一个数：response.numbers[0]。

##### return jsonify({"numbers": numbers}) 是 Flask 代码，它的作用是将数据列表以 JSON 格式返回给客户端。

##### jsonify 是 Flask 中内置的函数，即Ajax，它可以将 Python 对象转换为 JSON 格式，便于在客户端（如浏览器）与服务器端之间传递数据。

##### 在这个例子中，函数接受一个字典作为参数，该字典包含一个键 "numbers" 和数据列表作为值，最后返回该字典的 JSON 格式。

##### 当浏览器发送请求到服务器时，服务器会执行该代码，并返回随机数列表的 JSON 格式。浏览器接收到 JSON 数据后，可以使用 JavaScript 进行处理，并将数据显示在网页上。




