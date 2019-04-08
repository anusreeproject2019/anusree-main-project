from flask import *
import os
from werkzeug.utils import secure_filename
import MySQLdb
root=Flask(__name__)
root.secret_key="abc"
con=MySQLdb.Connect(host="localhost",user="root",passwd="",port=3306,db="paddy")
cmd=con.cursor()
path="C:\\Users\\hp\\PycharmProjects\\paddypronew\\web\\static\\articleupload"
path1="C:\\Users\\hp\\PycharmProjects\\paddypronew\\web\\static\\cropsinglerprt"
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
@root.route('/logout')
def logout():
    return render_template("login.html")
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
@root.route('/viewkbrprt')
def viewkbrprt():
    cmd.execute("select * from krishibhavan_report")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_krishibhavan_report.html",data=rslt)
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
    return render_template("view_farmer.html")
@root.route('/viewfarmers',methods=['GET','POST'])
def viewfarmers():
    farmer_id=request.form['textfield']
    farmer_name=request.form['textfield2']
    panchayath=request.form['textfield3']
    cmd.execute("select * from farmer_reg where fid='"+farmer_id+"'and farmer_name='"+farmer_name+"' and panchayath='"+panchayath+"'")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_farmer.html",data=rslt)
@root.route('/editfarmer')
def editfarmer():
    id=request.args.get('fid')
    session['idd']=id
    cmd.execute("select * from farmer_reg where fid='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("farmer_edit.html",val=s)
@root.route('/updatefarmer' ,methods=['GET','POST'])
def updatefarmer():
    Id=session['idd']
    farmer_name = request.form['textfield']
    gender = request.form['radiobutton']
    house = request.form['textfield3']
    place = request.form['textfield4']
    address = request.form['textarea']
    dictrict = request.form['select']
    phone = request.form['textfield7']
    email = request.form['textfield8']
    panchayath = request.form['select2']
    landmark = request.form['textfield10']
    crop = request.form['textfield11']
    type = request.form['textfield12']
    owner = request.form['textfield13']
    document = request.form['textfield14']
    cmd.execute("update farmer_reg set farmer_name='" + farmer_name + "',gender='" + gender + "',house='" + house + "',place='" + place + "',address='" + address + "',district='" + dictrict + "',phone='" + phone + "',email='" + email + "',panchayath='" + panchayath + "',landmark='" + landmark + "',crop='" + crop + "',type='" + type + "',owner='" + owner + "',document='" + document + "'")
    con.commit()
    return '''<script>alert("updated");window.location="/"</script>'''
@root.route('/deletefarmer')
def deletefarmer():
    id = request.args.get('fid')
    print(id)
    cmd.execute("delete from farmer_reg where fid='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/cropadd',methods=['GET','POST'])
def cropadd():
    return render_template('add_crop_details.html')
@root.route('/cropreg',methods=['GET','POST'])
def cropreg():
    crop_name=request.form['textfield']
    useful_for=request.form['textfield3']
    additional_info=request.form['textfield5']
    cmd.execute("insert into crop_info values(null,'" +crop_name+ "','"+useful_for+"','"+additional_info+"')")
    con.commit()
    return '''<script>alert("INSERTED");window.location="/kbhome"</script>'''
@root.route('/viewcrop')
def viewcrop():
    cmd.execute("select * from crop_info")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_crop_details.html",data=rslt)
@root.route('/editcrop')
def editcrop():
    id=request.args.get('crop_id')
    session['idd']=id
    cmd.execute("select * from crop_info where crop_id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("crop_edit.html",val=s)
@root.route('/updatecrop' ,methods=['GET','POST'])
def updatecrop():
    Id=session['idd']
    crop_name = request.form['textfield']
    useful_for = request.form['textfield3']
    additional_info = request.form['textfield5']
    cmd.execute("update crop_info set crop_name='"+crop_name+"',useful_for='"+useful_for+"',additional_info='"+additional_info+"' where crop_id='"+str(Id)+"'")
    con.commit()
    return '''<script>alert("updated");window.location="/kbhome"</script>'''
@root.route('/deletecrop')
def deletecrop():
    id = request.args.get('crop_id')
    print(id)
    cmd.execute("delete from crop_info where crop_id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/fertilizeradd',methods=['GET','POST'])
def fertilizeradd():
    return render_template('add_fertilizer_details.html')
@root.route('/ferlilizerreg',methods=['GET','POST'])
def fertilizerreg():
    fertilizer_name=request.form['textfield']
    useful_for=request.form['textfield3']
    quantity=request.form['textfield4']
    additional_info = request.form['textfield5']
    cmd.execute("insert into fertilizer_details values(null,'" +fertilizer_name+ "','"+useful_for+"','"+quantity+"','"+additional_info+"')")
    con.commit()
    return '''<script>alert("INSERTED");window.location="/kbhome"</script>'''
@root.route('/viewfertiliser')
def viewfertiliser():
    cmd.execute("select * from fertilizer_details")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_fertiliser_info.html",data=rslt)
@root.route('/editfertiliser')
def editfertiliser():
    id=request.args.get('fertiliser_id')
    session['idd']=id
    cmd.execute("select * from fertilizer_details where fertiliser_id='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("edit_fertiliser_details.html",val=s)
@root.route('/updatefertiliser' ,methods=['GET','POST'])
def updatefertiliser():
    Id=session['idd']
    fertilizer_name = request.form['textfield']
    useful_for = request.form['textfield3']
    quantity = request.form['textfield4']
    additional_info = request.form['textfield5']
    cmd.execute("update fertilizer_details set fertiliser_name='"+fertilizer_name+"',useful_for='"+useful_for+"',quantity='"+quantity+"',additional_info='"+additional_info+"' where fertiliser_id='"+str(Id)+"'")
    con.commit()
    return '''<script>alert("updated");window.location="/kbhome"</script>'''
@root.route('/deletefertiliser')
def deletefertiliser():
    id = request.args.get('fertiliser_id')
    print(id)
    cmd.execute("delete from fertilizer_details where fertiliser_id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/seedadd',methods=['GET','POST'])
def seedadd():
    return render_template('Add_seed_info.html')
@root.route('/seedreg',methods=['GET','POST'])
def seedreg():
    seed_name=request.form['textfield']
    type=request.form['textfield2']
    additional_info =request.form['textfield5']
    phone = request.form['textfield6']
    cmd.execute("insert into seed_info values(null,'" +seed_name+ "','"+type+"','"+additional_info+"','"+phone+"')")
    con.commit()
    return '''<script>alert("INSERTED");window.location="/kbhome"</script>'''
@root.route('/viewseed')
def viewseed():
    cmd.execute("select * from seed_info")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_seed_info.html",data=rslt)
@root.route('/editseed')
def editseed():
    id=request.args.get('sid')
    session['idd']=id
    cmd.execute("select * from seed_info where sid='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("edit_seed_info.html",val=s)
@root.route('/updateseed' ,methods=['GET','POST'])
def updateseed():
    Id=session['idd']
    seed_name = request.form['textfield']
    type = request.form['textfield2']
    additional_info = request.form['textfield5']
    phone = request.form['textfield6']
    cmd.execute("update seed_info set seed_name='"+seed_name+"',type='"+type+"',additional_info='"+additional_info+"',phone='"+phone+"' where sid='"+str(Id)+"'")
    con.commit()
    return '''<script>alert("updated");window.location="/kbhome"</script>'''
@root.route('/deleteseed')
def deleteseed():
    id = request.args.get('sid')
    print(id)
    cmd.execute("delete from seed_info where sid='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/pesticideadd',methods=['GET','POST'])
def pesticideadd():
    return render_template('Add_pesticide_info.html')
@root.route('/pesticidereg',methods=['GET','POST'])
def pesticidereg():
    pesticide_name=request.form['textfield']
    usefull_for=request.form['textfield3']
    quantity =request.form['textfield4']
    additional_info = request.form['textfield5']
    cmd.execute("insert into pesticide_details values(null,'" +pesticide_name+ "','"+usefull_for+"','"+quantity+"','"+additional_info+"')")
    con.commit()
    return '''<script>alert("INSERTED");window.location="/kbhome"</script>'''
@root.route('/viewpesticide')
def viewpesticide():
    cmd.execute("select * from pesticide_details")
    rslt=cmd.fetchall()
    print(rslt)
    return render_template("view_pesticide_info.html",data=rslt)
@root.route('/editpesiticide')
def editpesticide():
    id=request.args.get('pid')
    session['idd']=id
    cmd.execute("select * from pesticide_details where pid='"+str(id)+"'")
    s=cmd.fetchone()
    return render_template("edit_pesticide.html",val=s)
@root.route('/updatepesticide' ,methods=['GET','POST'])
def updatepesticide():
    Id=session['idd']
    pesticide_name = request.form['textfield']
    usefull_for = request.form['textfield3']
    quantity = request.form['textfield4']
    additional_info = request.form['textfield5']
    cmd.execute("update pesticide_details set pesticide_name='"+pesticide_name+"',usefull_for='"+usefull_for+"',quantity='"+quantity+"',additional_info='"+additional_info+"' where pid='"+str(Id)+"'")
    con.commit()
    return '''<script>alert("updated");window.location="/kbhome"</script>'''
@root.route('/deletepesticide')
def deletepesticide():
    id = request.args.get('pid')
    print(id)
    cmd.execute("delete from pesticide_details where pid='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted");window.location="/"</script>'''
@root.route('/singlereportadd',methods=['GET','POST'])
def singlereportadd():
    return render_template('add_single_report.html')
@root.route('/singlereportreg',methods=['GET','POST'])
def singlereportreg():
    farmer_name=request.form['textfield3']
    place=request.form['textfield4']
    crop =request.form['textfield5']
    photo = request.files['file']
    img=secure_filename(photo.filename)
    photo.save(os.path.join(path1,img))
    applied_fertiliser = request.form['textfield6']
    applied_pesticide = request.form['textfield7']
    detailed_report = request.form['textfield8']
    cmd.execute("insert into pesticide_details values(null,'" +farmer_name+ "','"+place+"','"+crop+"','"+img+"','"+applied_fertiliser+"','"+applied_pesticide+"','"+detailed_report+"')")
    con.commit()
    return '''<script>alert("INSERTED");window.location="/kbhome"</script>'''
if __name__=="__main__":
    root.run(debug=True)







