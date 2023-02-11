from flask import Flask, jsonify, render_template,Response
from time import time
import cv2

app = Flask(__name__)
t1=time()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def random_numbers():
   numbers=[round(time()-t1,1),
            0,
            0,
            0,
            0,
            0,
            0]#此列表为要显示的数据，当前为演示简单的demo，都设为0
   return jsonify({"numbers": numbers})#jsonify用于局部更新数据，与图像显示异步

class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(0) 
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

def gen(camera):
    while True:
        frame = camera.get_frame()
        #使用generator函数输出视频流，每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')#这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')#响应html的请求，返回视频流   

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)  
#网页查看输入：http://127.0.0.1:5000（只能本地查看）
#       或者：http://(本地ip地址):5000（可以其他主机查看）