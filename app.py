from flask import Flask,request
from flask.helpers import make_response
from flask.json import jsonify
import qrcode
import json
from PIL import Image
app = Flask(__name__)
app.config.from_pyfile("settings.py")

baseUrl = "http://10.0.2.2:5000"

@app.route("/home")
def home():
    list = []
    list.append(createPreviewItem(id=1,image="img1.png",title="叫了只鸡",deliver="起送￥10",deliverTime="配送约48分钟",lable="炸物小吃好评榜第2名",sale="月售1532"))
    list.append(createPreviewItem(id=2,image="img2.png",title="东北饺子馆",deliver="起送￥10",deliverTime="配送约53分钟",lable="近30天999+人复购",sale="月售5677"))
    list.append(createPreviewItem(id=3,image="img3.png",title="肥牛烤肉筋",deliver="起送￥12",deliverTime="配送约48分钟",lable="烧烤回头率第1名",sale="月售3078"))

    result = {
        "data":list,
        "msg": "请求成功"

    }
    return make_response(jsonify(result))

@app.route("/detail/<int:id>")
def detail(id):
    result={
        1:{
            "data":{
                "announce":"公告：炸鸡新款来了，肉和蘸料，口味，公司统一生产！",
                "list":[
                    createFood(1,1,"韩式炸鸡","门店销量第1名","月售656 好评度84%","15.95"),
                    createFood(2,1,"双拼口味炸鸡", "门店销量第2名", "月售336 好评度100%", "21.95"),
                    createFood(3,1,"香酥小酥肉", "小酥肉热榜第3名", "月售72 好评度98%", "5"),
                    createFood(1, 1, "韩式炸鸡2", "门店销量第1名", "月售656 好评度84%", "15.95"),
                    createFood(2, 1, "双拼口味炸鸡2", "门店销量第2名", "月售336 好评度100%", "21.95"),
                    createFood(3, 1, "香酥小酥肉2", "小酥肉热榜第3名", "月售72 好评度98%", "5"),
                ]
            }
        },
        2: {
            "data": {
                "announce": "公告：欢迎光临东北饺子馆 我们尽最大努力按照按时送达！",
                "list": [
                    createFood(1,2, "牛肉水饺24个", "门店销量第3名", "月售968 好评度100%", "14.98"),
                    createFood(2,2, "三陷混搭24个", "还行，吃的很饱", "月售402 好评度99%", "13.98"),
                    createFood(3,2, "韭菜鸡蛋水饺", "门店销量第1名", "月售1343 好评度95%", "4.5"),
                ]
            }
        },
        3: {
            "data": {
                "announce": "公告：下午16点到凌晨一点半都可以配送！",
                "list": [
                    createFood(1, 3, "半斤肉筋", "真香，香死了", "月售508 好评度100%", "22"),
                    createFood(2, 3, "翅中", "我室友特别喜欢", "月售355 好评度99%", "7"),
                    createFood(3, 3, "三肉筋+火腿+面筋+饼", "好吃美滋滋", "月售247 好评度95%", "14"),
                ]
            }
        },
    }
    result = result[id]
    return make_response(jsonify(result))
@app.route("/submit",methods=["POST"])
def submit():
    data = json.loads(request.get_data(as_text=True))
    img = qrcode.make(data)
    path = 'static/cart/'+"qr.png"
    img.save(path)
    result = {
        "msg":"上传成功",
        "path":baseUrl+"/"+path
    }
    return make_response(jsonify(result))

def createFood(id,parentId,title,lable,subTitle,price):
    return {
        "image": baseUrl+"/static/detail/"+str(parentId)+"/"+str(id)+".png",
        "name": title,
        "price": price,
        "subTitle": subTitle,
        "lable": lable
    }
def createPreviewItem(id,image,title,deliver,deliverTime,lable,sale):
    return {
        "id":id,
        "image":baseUrl+"/static/preview/"+image,
        "title":title,
        "deliver":deliver,
        "deliverTime":deliverTime,
        "lable":lable,
        "sale":sale,
        "detailUrl":baseUrl+"/detail/"+str(id)
    }