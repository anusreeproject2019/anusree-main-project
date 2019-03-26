from flask import *
import os
from werkzeug.utils import secure_filename
import MySQLdb
root=Flask(__name__)
root.secret_key="abc"
con=MySQLdb.Connect(host="localhost",user="root",passwd="",port=3306,db="paddy")
cmd=con.cursor()
path="C:\\Users\\hp\\PycharmProjects\\paddypronew\\web\\static\\articleupload"
@root.route('/')
def main():
    return render_template("login.html")
@root.route('/login',methods=['GET','POST'])
def login():
    username=request.form['textfield']
    password=request.form['textfield2']
    cmd.execute("select * from login where username='"+username+"' and password='"+password+"'")
    s=cmd.fetchone()
    print(s)
    if s is None:
        return '''<script>alert(Invalid);window.location="/"</script>'''
    elif s[1]=="admin":
        return '''<script>alert("successfully login");window.location="/home"</script>'''
    elif s[1]=="krishibhavan":
        return '''<script>alert("successfully login");window.location="/kbhome"</script>'''
@root.route('/home')
def home():
    return render_template("agricul_dep_home.html")
@root.route('/adhome')
def adhome():
    return render_template("agricul_dep_home.html")
@root.route('/kbhome')
def kbhome():
    return render_template("krishibhavan_home.html")
@root.route('/regview',methods=['GET','POST'])
def regview():
    return render_template('krishibhavan_reg.html')
@root.route('/reg',methods=['GET','POST'])
def reg():
  officer_name=request.form['textfield']
  email=request.form['textfield2']
  phone=request.form['textfield3']
  post=request.form['textfield4']
  district=request.form['select']
  panchayath=request.form['select2']
  pincode=request.form['textfield5']
  cmd.execute("insert into login values(null,'krishibhavan','"+email+"','"+phone+"')")
  id=con.insert_id()
  cmd.execute("insert into krishibhavan_reg values('"+str(id)+"','"+officer_name+"','"+email+"','"+phone+"','"+post+"','"+district+"','"+panchayath+"','"+pincode+"')")
  con.commit()
  return '''<script>alert("INSERTED");window.location="/home"</script>'''
@root.route('/viewkb')
def viewkb():
    cmd.execute("select * from krishibhavan_reg")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_krishibhavan.html",data=rslt)
@root.route('/edit')
def edit():
    id=request.args.get('kid')
    session['idd']=id
    cmd.execute("select * from krishibhavan_reg where kid='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("krishibhavan_edit.html",val=s)
@root.route('/update' ,methods=['GET','POST'])
def update():
    Id=session['idd']
    officer_name = request.form['textfield']
    email = request.form['textfield2']
    phone = request.form['textfield3']
    post = request.form['textfield4']
    district = request.form['select']
    panchayath = request.form['select2']
    pincode = request.form['textfield5']
    cmd.execute("update krishibhavan_reg set officer_name='"+officer_name+"',email='"+email+"',phone='"+phone+"',post='"+post+"',district='"+district+"',panchayath='"+panchayath+"',pincode='"+pincode+"' where kid='"+str(Id)+"'")
    con.commit()
    return '''<script>alert("updated");window.location="/"</script>'''
@root.route('/delete')
def delete():
    id = request.args.get('kid')
    print(id)
    cmd.execute("delete from krishibhavan_reg where kid='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/notview',methods=['GET','POST'])
def notview():
    return render_template('notification.html')
@root.route('/notification',methods=['GET','POST'])
def notification():
    title=request.form['textfield']
    date=request.form['textfield2']
    disease=request.form['textfield3']
    place=request.form['textfield4']
    plant=request.form['textfield5']
    symptoms=request.form['textfield6']
    cmd.execute("insert into notification values(null,'"+title+"','"+date+"','"+disease+"','"+place+"','"+plant+"','"+symptoms+"')")
    con.commit()
    return '''<script>alert("inserted");window.location="/"</script>'''
@root.route('/viewnot')
def viewnot():
    cmd.execute("select * from notification")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_notification.html",data=rslt)
@root.route('/editnot')
def editnot():
    id = request.args.get('nid')
    session['idd'] = id
    cmd.execute("select * from notification where nid='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template("notification_edit.html", val=s)
@root.route('/updatenot' ,methods=['GET','POST'])
def updatenot():
    Id=session['idd']
    title = request.form['textfield']
    date = request.form['textfield2']
    disease = request.form['textfield3']
    place = request.form['textfield4']
    plant = request.form['textfield5']
    symptoms = request.form['textfield6']
    cmd.execute("update notification set title='"+title+"',date='"+date+"',disease='"+disease+"',place='"+place+"',plant='"+plant+"',symptoms='"+symptoms+"' ")
    con.commit()
    return '''<script>alert("updated");window.location="/"</script>'''
@root.route('/deletenot')
def deletenot():
    id = request.args.get('nid')
    print(id)
    cmd.execute("delete from notification where nid='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/viewfeedback')
def viewfeedback():
    cmd.execute("select * from feedback")
    rslt = cmd.fetchall()
    print(rslt)
    return render_template("view_feedback.html", data=rslt)
@root.route('/policyview',methods=['GET', 'POST'])
def policyview():
    return render_template("add_govt_policies.html")
@root.route('/reggovtpolicy',methods=['GET','POST'])
def reggovtpolicy():
    policy_name=request.form['textfield']
    subject=request.form['textfield2']
    description=request.form['textfield4']
    date=request.form['textfield5']
    cmd.execute("insert into govt_policies values(null,'"+policy_name+"','"+subject+"','"+description+"','"+date+"')")
    con.commit()
    return '''<script>alert("inserted");window.location="/"</script>'''
@root.route('/viewgovtpolicy')
def viewgovtpolicy():
    cmd.execute("select * from govt_policies")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_govt_policy.html",data=rslt)
@root.route('/editgovtpolicy')
def editgovtpolicy():
    id = request.args.get('pid')
    session['idd'] = id
    cmd.execute("select * from govt_policies where pid='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template("govtpolicy_edit.html", val=s)
@root.route('/updatepolicy' ,methods=['GET','POST'])
def updatepolicy():
    Id=session['idd']
    policy_name = request.form['textfield']
    subject = request.form['textfield2']
    description = request.form['textfield4']
    date = request.form['textfield5']
    cmd.execute("update govt_policies set policy_name='"+policy_name+"',subject='"+subject+"',description='"+description+"',date='"+date+"' ")
    con.commit()
    return '''<script>alert("updated");window.location="/"</script>'''
@root.route('/deletepolicy')
def deletepolicy():
    id = request.args.get('pid')
    print(id)
    cmd.execute("delete from govt_policies where pid='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/viewfullrprt')
def viewfullrprt():
    return render_template("add_full_report.html")
@root.route('/addfullrprt',methods=['GET','POST'])
def addfullrprt():
    crop = request.form['textfield']
    place = request.form['textfield2']
    noof_disease = request.form['textfield3']
    symptoms = request.form['textfield4']
    action = request.form['textfield5']
    cmd.execute("insert into admin_full_report values(null,'" +crop+ "','" +place+ "','" +noof_disease+ "','" +symptoms+ "','"+action+"')")
    con.commit()
    return '''<script>alert("inserted");window.location="/"</script>'''
@root.route('/viewfullreport')
def viewfullreport():
    cmd.execute("select * from admin_full_report")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_fullrprt.html",data=rslt)
@root.route('/editfullrprt')
def editfullrprt():
    id = request.args.get('frepo_id')
    session['idd'] = id
    cmd.execute("select * from admin_full_report where frepo_id='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template("edit_full_report.html", val=s)
@root.route('/updatefullrprt' ,methods=['GET','POST'])
def updatefullrprt():
    crop = request.form['textfield']
    place = request.form['textfield2']
    noof_disease = request.form['textfield3']
    symptoms = request.form['textfield4']
    action = request.form['textfield5']
    cmd.execute("update admin_full_report set crop='"+crop+"',place='"+place+"',noof_disease='"+noof_disease+"',symptoms='"+symptoms+"',action='"+action+"' ")
    con.commit()
    return '''<script>alert("updated");window.location="/"</script>'''
@root.route('/deletefullrprt')
def deletefullrprt():
    id = request.args.get('frepo_id')
    print(id)
    cmd.execute("delete from admin_full_report where frepo_id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/viewarticle')
def viewarticle():
    return render_template("add_article.html")
@root.route('/addarticle',methods=['GET','POST'])
def addarticle():
    article_title = request.form['textfield']
    description = request.form['textfield2']
    file = request.files['file']
    img=secure_filename(file.filename)
    file.save(os.path.join(path,img))
    cmd.execute("insert into article_add values(null,'" +article_title+ "','" +description+ "','" +img+ "')")
    con.commit()
    return '''<script>alert("file added");window.location="/"</script>'''
@root.route('/articleview')
def articleview():
        cmd.execute("select * from article_add")
        rslt = cmd.fetchall()
        print(rslt)
        return render_template("view_article.html", data=rslt)
        return '''<script>alert("inserted");window.location="/"</script>'''
@root.route('/editarticle')
def editarticle():
    id = request.args.get('aid')
    session['idd'] = id
    cmd.execute("select * from article_add where aid='" + str(id) + "'")
    s = cmd.fetchone()
    return render_template("edit_article.html", val=s)
@root.route('/updatearticle' ,methods=['GET','POST'])
def updatearticle():
    article_title = request.form['textfield']
    description = request.form['textfield2']
    file = request.files['file']
    img = secure_filename(file.filename)
    file.save(os.path.join(path, img))
    cmd.execute("update article_add set article_title='"+article_title+"',description='"+description+"',file='"+img+"' ")
    con.commit()
    return '''<script>alert("updated");window.location="/"</script>'''
@root.route('/deletearticle')
def deletearticle():
    id = request.args.get('aid')
    print(id)
    cmd.execute("delete from article_add where aid='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/fregview',methods=['GET','POST'])
def fregview():
    return render_template('farmer_reg.html')
@root.route('/farmereg',methods=['GET','POST'])
def farmereg():
    farmer_name=request.form['textfield']
    gender=request.form['radiobutton']
    house=request.form['textfield3']
    place=request.form['textfield4']
    address=request.form['textarea']
    dictrict=request.form['select']
    phone=request.form['textfield7']
    email=request.form['textfield8']
    panchayath=request.form['select2']
    landmark=request.form['textfield10']
    crop=request.form['textfield11']
    type=request.form['textfield12']
    owner=request.form['textfield13']
    document=request.form['textfield14']
    cmd.execute("insert into farmer_reg values(null,'" +farmer_name+ "','" +gender+ "','" +house+ "','" +place+ "','"+address+"','"+dictrict+"','"+phone+"','"+email+"','"+panchayath+"','"+landmark+"','"+crop+"','"+type+"','"+owner+"','"+document+"')")
    con.commit()
    return '''<script>alert("INSERTED");window.location="/kbhome"</script>'''
@root.route('/viewfarmer')
def viewfarmer():
    cmd.execute("select * from farmer_reg")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_farmer.html",data=rslt)
if __name__=="__main__":
    root.run(debug=True)







