from flask import *
from werkzeug.utils import secure_filename

from src.dbconnection import *

app=Flask(__name__)


@app.route("/logincode",methods=['post'])
def logincode():
    uname = request.form['uname']
    print(uname)
    password = request.form['password']
    print(password)
    q = "select * from login where username=%s and password=%s"
    val =( uname, password)
    res = selectonenew(q, val)
    print(res)
    if res is None:
        return jsonify({'task': 'invalid'})
    else:
        print(res[3])
        if res[3]=='parent':
            qry="SELECT `student`.`login_id` FROM `student` JOIN `parent` ON `parent`.`admission_number`=`student`.`roll_no` WHERE `parent`.`login_id`=%s"
            val=str(res[0])
            ress=selectonenew(qry,val)
            return jsonify({'task': "success", 'type': res[3], 'id': ress[0]})

        return jsonify({'task':"success",'type': res[3],'id':res[0]})


@app.route("/viewattendance",methods=['post'])
def viewattendance():
    lid=request.form['lid']
    print(lid)

    # qry1="SELECT `parent`.`admission_number` FROM `parent` WHERE `parent`.`login_id`=%s"
    # val=str(lid)
    # res =selectonenew(qry1,val)
    # sid=str(res[0])
    # print(sid)

    qry="SELECT `student`.`first_name`,`last_name`,COUNT(`attendance`.id) as twd,SUM(`attendance`.`attendance`) as tpd,(SUM(`attendance`.`attendance`)/COUNT(`attendance`.id))*100 as p FROM `student`  JOIN `attendance` ON `student`.`login_id`=`attendance`.`stud_id` WHERE  `student`.`login_id`=%s"
    print(qry)
    val=(lid)
    res=androidselectall(qry,val)
    print(res)

    return jsonify(res)

@app.route("/viewmark",methods=['post'])
def viewmark():
    lid=request.form['lid']
    qry="SELECT `mark`.`mark`,`subject`.`subject` FROM `mark` JOIN `subject` ON (`mark`.`sub_id`=`subject`.`sub_id`)WHERE `mark`.`stud_id`=%s"
    val=(lid)
    res = androidselectall(qry,val)
    return jsonify(res)
@app.route("/viewmarkparent",methods=['post'])
def viewmarkparent():
    lid=request.form['lid']
    qry="SELECT `mark`.`mark`,`subject`.`subject` FROM `mark` JOIN `subject` ON (`mark`.`sub_id`=`subject`.`sub_id`)WHERE `mark`.`stud_id`=%s"
    val=(lid)
    res = androidselectall(qry,val)
    return jsonify(res)
@app.route("/addfeedback",methods=['post'])
def addfeedback():
    print(request.form)
    stud_id=request.form['lid']
    feedback=request.form['feedback']
    qry="insert into feedback values(null,%s,curdate(),%s)"
    val=(stud_id,feedback)
    iud(qry,val)
    return jsonify({'task': 'success'})

@app.route("/performanceprediction",methods=['post'])
def performanceprediction():
    lid=request.form['studid']
    qry="SELECT `mark`.`mark`,`subject`.`subject` FROM `mark` JOIN `subject` ON (`mark`.`sub_id`=`subject`.`sub_id`)WHERE `mark`.`stud_id`=%s"
    val=(lid)
    res=selectallnew(qry,val)

    qry = "SELECT `student`.`first_name`,`last_name`,COUNT(`attendance`.id) as twd,SUM(`attendance`.`attendance`) as tpd,(SUM(`attendance`.`attendance`)/COUNT(`attendance`.id))*100 as p FROM `student`  JOIN `attendance` ON `student`.`login_id`=`attendance`.`stud_id` WHERE  `student`.`login_id`=%s"
    print(qry)
    val = (lid)
    res1 = selectonenew(qry, val)
    att=res1[4]

    rh=["attendance","mark","avgs","subject"]
    resss=[]
    for r in range(0,len(res)):
        row=[]
        row.append(att)
        row.append(res[r][0])
        rr=float(att)+(float(res[r][0])/50)*100
        row.append(str(rr))
        row.append(res[r][1])
        resss.append(dict(zip(rh, row)))
    print(resss)
    return jsonify(resss)


@app.route("/addparent",methods=['post'])
def addparent():
    first_name=request.form['fname']
    last_name=request.form['lname']
    admission_number=request.form['admno']
    contact_no=request.form['contactno']
    username=request.form['username']
    password=request.form['password']
    qry = "insert into login values(null,%s,%s,'parent')"
    value = (username, password)
    lid = iud(qry, value)
    qry1 = "insert into parent values(null,%s,%s,%s,%s,%s)"
    val = (str(lid), first_name,last_name,admission_number,contact_no)
    iud(qry1, val)
    return jsonify({'task': 'success'})

@app.route("/viewremarks",methods=['post'])
def viewremarks():
    lid = request.form['lid']
    print(lid)
    qry1 = "SELECT `student`.`login_id` FROM `student` JOIN `parent` ON `parent`.`admission_number`=`student`.`roll_no` WHERE `student`.`login_id`=%s"
    val1=str(lid)
    ress = selectonenew(qry1, val1)
    sid=ress[0]
    qry = "SELECT * FROM remark WHERE `stud_id`=%s"
    val = (str(sid))
    res = androidselectall(qry, val)
    print(res)
    return jsonify(res)


@app.route('/performance', methods=['get', 'post'])
def performance():
    studid=request.form['studid']
    print(studid)
    qry="SELECT `student`.`first_name`,`student`.`last_name`,`student`.`login_id`,ROUND((SUM(`attendance`)/COUNT(*))*100) AS attendance,ROUND((SUM(`mark`)/(COUNT(*)*20))*100) AS `mark`, ROUND((((SUM(`attendance`)/COUNT(*))*100)+(SUM(`mark`)/(COUNT(*)*20))*100)/2) AS avgs FROM `attendance` JOIN `student` ON `student`.`login_id`=`attendance`.`stud_id` JOIN `mark`  ON `student`.`login_id`=`mark`.`stud_id` WHERE `student`.`login_id`=%s GROUP BY `attendance`.`Stud_id`,mark.stud_id  "
    val=(studid)
    s=androidselectall(qry,val)
    return jsonify(s)


app.run(host="0.0.0.0",port=5000)