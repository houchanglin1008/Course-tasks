from flask import Flask,jsonify,abort,make_response,render_template
from flask_httpauth import HTTPBasicAuth
from mysql import Mysql
import time
import utlis
import re
from judje import JudjeTime

app = Flask(__name__)

@app.route('/favicon.ico')
def get_fav():
    return app.send_static_file('favicon.ico')

@app.route('/',methods=['GET'])
def get_home():
    job = JudjeTime().judje()
    if job == True:
        abort(403)
    db = Mysql()
    items = db.get_pro_id()
    return render_template('index.html',items=items)

@app.route('/l1',methods=['GET'])
def get_l1_num():
    job = JudjeTime().judje()
    if job == True:
        abort(403)
    db = Mysql()
    items = db.get_l1_Items()[-1]
    df = db.get_l1_Items()[-2]
    data = [{"pigprice":items[0]},{"pig_in":items[1]},{"pig_local":items[2]},{"maize":items[3]},{"bean":items[4]}]
    da = [{"pigprice":df[0]},{"pig_in":df[1]},{"pig_local":df[2]},{"maize":df[3]},{"bean":df[4]}]
    bar = [items[0],items[1],items[2]]
    return jsonify({'data':data,'df':da,'bar':bar})
	
@app.route('/b',methods=['GET'])
def get_b1():
    job = JudjeTime().judje()
    if job == True:
        abort(403)
    db = Mysql()
    items = db.get_l1_Items()
    date,pigprice,pig_in,pig_local,maize,bean = [],[],[],[],[],[]
    for a in items:
        date.append('%s'%a[5])
        pigprice.append(a[0])
        pig_in.append(a[1])
        pig_local.append(a[2])
        maize.append(a[3])
        bean.append(a[4])
    return jsonify({"pigprice":pigprice,"date":date,"pig_in":pig_in,"pig_local":pig_local,"maize":maize,"bean":bean})

@app.route('/r3',methods=['GET'])
def get_r3():
    job = JudjeTime().judje()
    if job == True:
        abort(403)
    db = Mysql()
    items = db.get_l1_Items()[-30:-1]
    date,pigprice,pig_in,pig_local,maize,bean = [],[],[],[],[],[]
    for a in items:
        date.append('%s'%a[5])
        pigprice.append(a[0])
        pig_in.append(a[1])
        pig_local.append(a[2])
        maize.append(a[3])
        bean.append(a[4])
    return jsonify({"pigprice":pigprice,"date":date,"pig_in":pig_in,"pig_local":pig_local,"maize":maize,"bean":bean})

@app.route('/map',methods=['GET'])
def get_map():
    job = JudjeTime().judje()
    if job == True:
        abort(403)
    db = Mysql()
    items = db.get_pro_id()
    data = []
    for item in items:
        df = db.get_map_Items(item[1])
        na=re.findall(r'(.*?)(省|市)',item[0])
        if na == []:
            name = item[0]
        else:
            name = item[0][:-1]
        pigprice=df[-1][1]
        data.append({"name":name,"value":pigprice})
    return jsonify({"data":data})

@app.route('/time',methods=['GET'])
def get_time():
    job = JudjeTime().judje()
    if job == True:
        abort(403)
    return utlis.get_time()

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    job = JudjeTime().judje()
    if job == True:
        abort(403)
    db = Mysql()
    items = db.get_map_Items(task_id)[-30:]
    date,pigprice,pig_in,pig_local,maize,bean = [],[],[],[],[],[]
    for a in items:
        date.append('%s'%a[6])
        pigprice.append(a[1])
        pig_in.append(a[2])
        pig_local.append(a[3])
        maize.append(a[4])
        bean.append(a[5])
    return jsonify({"pigprice":pigprice,"date":date,"pig_in":pig_in,"pig_local":pig_local,"maize":maize,"bean":bean})

@app.errorhandler(403)
def not_found(error):
    return make_response(render_template('notfound.html'), 403)

if __name__ =='__main__':
    app.run(debug=True,port=5000)