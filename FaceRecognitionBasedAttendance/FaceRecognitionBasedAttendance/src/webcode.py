from flask import *
from werkzeug.utils import secure_filename

from src.dbconnection import *

app=Flask(__name__)
app.secret_key="abc"
@app.route('/')
def main():
    # return render_template("index.html")
    return render_template("login.html")

@app.route("/loginnew",methods=['post'])
def loginnew():
    uname=request.form['textfield']
    passwd=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(uname,passwd)
    res=selectonenew(qry,val)
    print(res,"===========")
    if res is None:
        return'''<script>alert("invalid");window.location="/"</script>'''
    elif res[3]=="admin":
        return '''<script>alert("login success");window.location="/adminhome"</script>'''
    elif res[3]=="teacher":
        return'''<script>alert("login success");window.location="/staffhome"</script> '''
    else:
        return'''<script>alert("invalid");window.location="/"</script>'''


@app.route('/adddepartment',methods=['post'])
def adddepartment():
    return render_template("Admin/add department.html")

@app.route('/adminhome')
def adminhome():
    return render_template("Admin/admin home.html")

@app.route('/addstudent',methods=['post'])
def addstudent():
    qry="select * from department"
    res1=selectall(qry)
    return render_template("Admin/Add student.html",data1=res1)

@app.route('/addstudentcode',methods=['post'])
def addstudentcode():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    admission=request.form['textfield3']
    gender=request.form['radiobutton']
    course=request.form['select']
    sem=request.form['select2']
    dob=request.form['textfield12']
    photo=request.files['file']
    filename=secure_filename(photo.filename)
    photo.save('static/photos/'+filename)
    hname=request.form['textfield4']
    dist=request.form['textfield5']
    place=request.form['textfield6']
    post=request.form['textfield7']
    pin=request.form['textfield8']
    contactno=request.form['textfield9']
    mail=request.form['textfield10']
    password=request.form['textfield11']
    qry="insert into login values(null,%s,%s,'student')"
    vals=(mail,password)
    lid=iud(qry,vals)
    qry = "insert into student values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    vals =(str(lid),fname,lname,admission,course,sem,filename,dob,gender,hname,dist,place,post,pin,contactno)
    iud(qry, vals)
    return '''<script>alert("registration success");window.location="/viewstudent"</script>'''

@app.route('/addteacher',methods=['post'])
def addteacher():
    qry="select * from department"
    res=selectall(qry)
    return render_template("Admin/Add teacher.html",data=res)


@app.route('/viewdepartment')
def viewdepartment():
    qry = "SELECT * FROM department"
    res = selectall(qry)
    return render_template("Admin/view department.html",data=res)

@app.route('/viewstudent')
def viewstudent():

    qry="select * from department"
    res1=selectall(qry)
    qry = "SELECT * FROM student"
    res = selectall(qry)
    return render_template("Admin/View student.html",data=res,data1=res1)

@app.route('/viewteacher')
def viewteacher():
    qry="select * from department"
    res1=selectall(qry)
    qry="SELECT * FROM teacher"
    res=selectall(qry)
    return render_template("Admin/View teacher.html",data=res,data1=res1)

@app.route('/staffhome')
def staffhome():
    return render_template("Staff/staff home.html")

@app.route('/addcomments',methods=['post','get'])
def addcomments():
    qry="select * from student"
    res=selectall(qry)

    return render_template("Staff/add comments.html",data=res)

@app.route('/addcommentscode',methods=['post'])
def addcommentscode():
    roll_no=request.form['select']
    comment=request.form['textfield2']
    qry="insert into remark values(null,%s,curdate(),%s)"
    vals=(roll_no,comment)
    iud(qry,vals)

    return '''<script>alert("comments added");window.location="/addcomments"</script>'''





@app.route('/addinternalmark',methods=['post','get'])
def addinternalmark():
    qry="select * from department"
    res=selectall(qry)
    return render_template("Staff/add internal mark.html",data=res,c='',s='')


@app.route('/addinternalmarksearch',methods=['post'])
def addinternalmarksearch():
    type=request.form['Submit']
    if type=="Search":
        course=request.form['select']
        semester=request.form['select2']
        qry="SELECT `student`.* FROM `student` JOIN `department` ON `student`.`dept_id`=`department`.`id` WHERE `student`.`dept_id`=%s AND `student`.`semester`=%s"
        val=(course,semester)
        res=selectallnew(qry,val)
        qry="SELECT * FROM `subject`  WHERE `dep_id`=%s AND `sem`=%s"
        val=(course,semester)
        res1=selectallnew(qry,val)

        qry = "select * from department"
        res2 = selectall(qry)
        return render_template("Staff/add internal mark.html",res=res,res1=res1,data=res2,c=str(course),s=str(semester))
    else:
        course = request.form['select']
        semester = request.form['select2']
        subject = request.form['select3']
        qry = "SELECT `student`.* FROM `student` JOIN `department` ON `student`.`dept_id`=`department`.`id` WHERE `student`.`dept_id`=%s AND `student`.`semester`=%s"
        val = (course, semester)
        res = selectallnew(qry, val)
        for i in res:
            mark=request.form[str(i[1])]
            qry="INSERT INTO `mark` VALUES(NULL,%s,%s,%s)"
            val=(str(i[1]),mark,subject)
            iud(qry,val)
        return '''<script>alert("mark added");window.location="/addinternalmark"</script>'''


@app.route('/addinternalmarkcode',methods=['post'])
def addinternalmarkcode():
    btn=request.form['Submit']
    cid=request.form['select']
    sem=request.form['select2']

@app.route('/viewinternalmark',methods=['post','get'])
def viewinternalmark():
    qry="select * from department"
    res=selectall(qry)
    qry="select * from subject"
    res1=selectall(qry)

    return render_template("Staff/view internal mark.html",data=res,data1=res1,c='',s='')

@app.route('/viewinternalmarksearch',methods=['post'])
def viewinternalmarksearch():
    course=request.form['select']
    sem=request.form['select2']
    subject=request.form['select3']
    qry="SELECT * FROM `mark` JOIN `student`ON (`student`.`login_id`=`mark`.`stud_id`) WHERE `sub_id`=%s"
    val=(subject)
    res3=selectallnew(qry,val)
    qry = "select * from department"
    res = selectall(qry)
    qry = "select * from subject"
    res1 = selectall(qry)


    return render_template("staff/view internal mark.html",data=res,data1=res1,data3=res3)






@app.route('/addsubject',methods=['post'])
def addsubject():
    qry="select * from department"
    res=selectall(qry)
    return render_template("Staff/Add subject.html",data=res)

@app.route('/addsubjectcode',methods=['post'])
def addsubjectcode():
    dep_id=request.form['select1']
    sem=request.form['select2']
    subject=request.form['textfield']
    qry="insert into subject values(null,%s,%s,%s)"
    vals=(dep_id,sem,subject)
    iud(qry,vals)
    return '''<script>alert("subject added");window.location="/viewsubject"</script>'''



@app.route('/editattendance')
def editattendance():
    return render_template("Staff/edit attendance.html")




@app.route('/editmark')
def editmark():
    return render_template("Staff/edit mark.html")




@app.route('/performancegrade')
def performancegrade():
    qry="select * from department"
    res=selectall(qry)
    print(res)

    return render_template("Staff/performance grade.html",data=res)

@app.route('/performancegrade1',methods=['post'])
def performancegrade1():
    course=request.form['select']
    semester=request.form['select2']
    qry = "select * from department"
    res1 = selectall(qry)

    qry="SELECT *FROM `student` WHERE `dept_id`=%s AND `semester`=%s"
    val=(course,semester)
    res=selectallnew(qry,val)
    print(res)
    return render_template("Staff/performance grade.html",res=res,data=res1)

@app.route('/performancegradeview')
def performancegradeview():
    lid=request.args.get('id')

    qry = "SELECT `mark`.`mark`,`subject`.`subject` FROM `mark` JOIN `subject` ON (`mark`.`sub_id`=`subject`.`sub_id`)WHERE `mark`.`stud_id`=%s"
    val = (lid)
    res = selectallnew(qry, val)

    qry = "SELECT `student`.`first_name`,`last_name`,COUNT(`attendance`.id) as twd,SUM(`attendance`.`attendance`) as tpd,(SUM(`attendance`.`attendance`)/COUNT(`attendance`.id))*100 as p FROM `student`  JOIN `attendance` ON `student`.`login_id`=`attendance`.`stud_id` WHERE  `student`.`login_id`=%s"
    print(qry)
    val = (lid)
    res1 = selectonenew(qry, val)
    att = res1[4]

    rh = ["attendance", "mark", "avgs", "subject"]
    resss = []
    for r in range(0, len(res)):
        row = []

        avg = (float(att) + (float(res[r][0]) / 50) * 100)/2

        row.append(res[r][1])

        if (avg > 90):
            row.append("A");
        elif (avg > 80):
                row.append("B");

        elif (avg > 70):
                    row.append("C");

        elif (avg > 60):
             row.append("D");
        elif (avg >= 50):
               row.append("E");

        else:
            row.append("F");


        resss.append(row)
    print(resss)
    return render_template("Staff/performance grade view.html",val=resss)




@app.route('/viewattendance',methods=['post','get'])
def viewattendance():
    qry="select * from department"
    res=selectall(qry)

    return render_template("Staff/view attendance.html",data=res)

@app.route('/viewattendancesearch',methods=['post'])
def viewattendancesearch():
    course=request.form['select']
    sem=request.form['select2']
    qry="SELECT `student`.`first_name`,`last_name`,COUNT(`attendance`.id),SUM(`attendance`.`attendance`),(SUM(`attendance`.`attendance`)/COUNT(`attendance`.id))*100 FROM `student`  JOIN `attendance` ON `student`.`login_id`=`attendance`.`stud_id` WHERE `student`.`dept_id`=%s AND `student`.`semester`=%s GROUP BY `student`.`login_id`"
    val=(course,sem)
    res1=selectallnew(qry,val)
    qry = "select * from department"
    res = selectall(qry)
    return render_template("Staff/view attendance.html", data1=res1,data=res,c=str(course),s=str(sem))

@app.route('/viewattendancebydate')
def viewattendancebydate():
    return render_template("Staff/View attendance by date.html")


@app.route('/viewcomments')
def viewcomments():
    return render_template("Staff/view comments.html")

@app.route('/viewfeedback',methods=['post','get'])
def viewfeedback():
    qry="SELECT * FROM feedback JOIN  student ON (`student`.id=`feedback`.`stud_id`)"

    res=selectall(qry)
    return render_template("Staff/view feedback.html",data=res)



@app.route('/viewsubject')
def viewsubject():
    qry="SELECT `department`.`d_name`,`subject`.* FROM `subject` JOIN `department` ON  `department`.`id`=`subject`.`dep_id`"
    res=selectall(qry)
    return render_template("Staff/View subject.html",data=res)

@app.route('/editsubject',methods=['get','post'])
def editsubject():
    id=request.args['id']
    session['eid']=id
    qry="select * from subject join department on (department.id=subject.dep_id) where sub_id=%s"
    values=(id)
    res=selectonenew(qry,values)
    qry="select * from department"
    res1=selectall(qry)
    return render_template("Staff/edit subject.html",data=res,data1=res1)

@app.route('/updatesubject',methods=['post'])
def updatesubject():
    dep_id = request.form['select1']
    sem = request.form['select2']
    subject = request.form['textfield']
    qry = "update subject set sem=%s,subject=%s where sub_id=%s"
    vals = (sem, subject,str(session['eid']))
    iud(qry,vals)
    return '''<script>alert("subject updated");window.location="/viewsubject"</script>'''

@app.route('/deletesubject',methods=['post','get'])
def deletesubject():
    id = request.args['id']
    qry = "delete from subject where sub_id=%s"
    val = (id)
    iud(qry, val)
    return '''<script>alert("deletion successful");window.location="/viewsubject"</script>'''


@app.route('/editstudent',methods=['get'])
def editstudent():
    id=request.args['id']
    session['eid']=id
    qry="select * from department"
    res1=selectall(qry)
    qry="select * from student where login_id=%s"
    values=(id)
    res=selectonenew(qry,values)
    return render_template("Admin/edit student.html",data=res,data1=res1)

@app.route('/updatestudent',methods=['post'])
def updatestudent():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    admission = request.form['textfield3']
    course = request.form['select']
    sem = request.form['select2']
    dob = request.form['textfield12']
    hname = request.form['textfield4']
    dist = request.form['textfield5']
    place = request.form['textfield6']
    post = request.form['textfield7']
    pin = request.form['textfield8']
    contactno = request.form['textfield9']
    qry = "update student set first_name=%s,last_name=%s,roll_no=%s,dept_id=%s,semester=%s,date_of_birth=%s,address=%s,district=%s,place=%s,post=%s,pin=%s,contactno=%s where login_id=%s"
    vals = (
    fname, lname, admission, '445', sem, dob, hname, dist, place, post, pin, contactno,session['eid'])
    iud(qry, vals)
    return '''<script>alert("registration success");window.location="/viewstudent"</script>'''



@app.route('/deletestudent')
def deletestudent():
    id = request.args['id']
    qry="delete from student where login_id=%s"
    val=(id)
    iud(qry,val)
    return'''<script>alert("deletion successful");window.location="/viewstudent"</script>'''



@app.route('/addcoursecode',methods=['post'])
def addcoursecode():
    d_name=request.form['textfield']
    qry="insert into department values(null,%s)"
    vals=(d_name)
    iud(qry,vals)
    return '''<script>alert("course succesfully added");window.location="/viewdepartment"</script>'''

@app.route('/editdepartment',methods=['post','get'])
def editdepartment():
    id = request.args['id']
    session['eid'] = id
    qry = "select * from department where id=%s"
    values = (id)
    res = selectonenew(qry, values)
    return render_template("Admin/edit department.html",v=res)

@app.route('/updatedepartment',methods=['post'])
def updatedepartment():
    d_name=request.form['textfield']
    qry="update department set d_name=%s where id=%s"
    vals=(d_name,str(session['eid']))
    iud(qry,vals)
    return'''<script>alert("updation success");window.location="/viewdepartment"</script>'''



@app.route('/addstaffcode',methods=['post'])
def addstaffcode():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    gender=request.form['radiobutton']
    address=request.form['textfield4']
    district=request.form['textfield5']
    place=request.form['textfield6']
    post=request.form['textfield7']
    pin=request.form['textfield8']
    contact_no=request.form['textfield9']
    mail=request.form['textfield10']
    dep_id=request.form['select']
    username=request.form['textfield3']
    password=request.form['textfield11']
    qry = "insert into login values(null,%s,%s,'teacher')"
    vals = (username,password)
    lid = iud(qry, vals)
    qry = "insert into teacher values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    vals=(fname,lname,gender,address,district,place,post,pin,contact_no,mail,dep_id)
    iud(qry, vals)
    return '''<script>alert("staff succesfully added");window.location="/viewteacher"</script>'''


@app.route("/liststudent",methods=['post'])
def liststudent():
    qry="select * from department"
    res1=selectall(qry)
    course=request.form['select']
    sem=request.form['select2']
    qry="SELECT * FROM student WHERE dept_id=%s AND semester=%s"
    val=(course,sem)
    res=selectallnew(qry,val)
    return render_template("Admin/View student.html", data=res,data1=res1)


@app.route("/listteacher",methods=['post'])
def listteacher():
    qry="select * from department"
    res1=selectall(qry)
    department=request.form['select']
    qry="SELECT * FROM teacher WHERE dep_id=%s"
    val=(department)
    res=selectallnew(qry,val)
    return render_template("Admin/View teacher.html", data=res,data1=res1)


@app.route('/deleteteacher')
def deleteteacher():
    id = request.args['id']
    qry="delete from teacher where teacher_id=%s"
    val=(id)
    iud(qry,val)
    return'''<script>alert("deletion successful");window.location="/viewteacher"</script>'''

@app.route('/deletedepartment')
def deletedepartment():
    id = request.args['id']
    qry="delete from department where id=%s"
    val=(id)
    iud(qry,val)
    return'''<script>alert("deletion successful");window.location="/viewdepartment"</script>'''




app.run(debug=True)
