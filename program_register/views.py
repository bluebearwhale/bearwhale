from django.shortcuts import render,redirect
import pyrebase
from django.contrib import auth
import calendar
import datetime
config={
    'apiKey': "AIzaSyDsCCUMuEWG2Z0muC86Jf0WMr6VWA3NHe0",
    'authDomain': "program-register.firebaseapp.com",
    'databaseURL': "https://program-register.firebaseio.com",
    'projectId': "program-register",
    'storageBucket': "program-register.appspot.com",
    'messagingSenderId': "260341568372",
    'appId': "1:260341568372:web:2506fd091d30e6fad11221",
    'measurementId': "G-3NJW7KE5YC"
    
}

firebase = pyrebase.initialize_app(config)

authe=firebase.auth()
database=firebase.database()

this_month=datetime.datetime.now().month
this_year=datetime.datetime.now().year
last_date=calendar.monthrange(this_year,this_month)[1]

register_people=[]
names=[]#확정자 명
def ordering():
    this_month_date=[]
    order1=[]
    order2=[]
    input_t1=[]
    input_t2=[]
    for i in range(last_date):

        names.append('')
        order1.append('')
        order2.append('')
        input_t1.append('')
        input_t2.append('')

        this_month_date.append(i+1)
    
    registerd=database.child('register').get()

    
    for da in range(last_date):
        try:
            uids=database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(da)).get()
            for uid in uids.each():
                tem_name=database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(da)).child(uid.key()).child('chd_name').get().val()
                tem_input=database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(da)).child(uid.key()).child('input time').get().val()
                tem_people=database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(da)).child(uid.key()).child('people').get().val()
                if input_t1[da] =='':
                    order1[da]=tem_name+'('+str(tem_people)+')'
                    input_t1[da]=tem_input
                else:
                    if input_t1[da]>tem_input:
                        print(input_t1[da]>tem_input)
                        if iinput_t2[da] =='':
                            order2[da]=order1[da]
                            input_t2[da]=input_t1[da]
                            
                            order1[da]=tem_name+'('+tem_people+')'
                            input_t1[da]=tem_input
                        else:
                            if input_t2[da] >tem_input:
                                print(input_t2[da] >tem_input)
                               
                                order2[da]=tem_name+'('+tem_people+')'
                                input_t2[da]=tem_input
                    else:
                        if input_t2[da] =='':
                            order1[da]=tem_name+'('+tem_people+')'
                            input_t1[da]=tem_input
                        else:
                            if input_t2[da] >tem_input:
                                print(input_t2[da] >tem_input)
                               
                                order2[da]=tem_name+'('+tem_people+')'
                                input_t2[da]=tem_input


        except:
            pass
    return this_month_date,order1, order2

def signIn(request):

    return render(request,'signIn.html')

def postsign(request):
    '''
    order1=[]
    order2=[]
    input_t1=[]
    input_t2=[]
    '''
    email=request.POST.get('email')
    passw=request.POST.get("pass")
    try:
        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
        return render(request,'signIn.html',{'mssg':message})
    #print(user['idToken'])
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    try:
        idtoken= request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        name = database.child('users').child(a).child('details').child('name').get().val()
        email=name
    except:
        pass
    temp=database.child('register').get()
    
    ##################################################월을 받아서 화면에 뿌려주기
    '''
    for i in range(last_date):
        names.append('')
        order1.append('')
        order2.append('')
        input_t1.append('')
        input_t2.append('')

        this_month_date.append(i+1)
    
    registerd=database.child('register').get()
    #register_people[i].append(registerd)
    #try:
    '''
    '''
    for c in temp.each():
        tem=datetime.datetime.strptime(c.key(),"%Y-%m-%d").date()
        if tem.month==this_month:
            print(c.key())
            print(database.child('register').child(c.key()).get().val())
            print(c.val())
    '''
    '''
    for da in range(last_date):
        try:
            uids=database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(da)).get()
            for uid in uids.each():
                print(database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(i)).child(uid.key()).child('name').get().val())
                print(str(this_year)+'-'+str(this_month)+'-'+str(da))
                
                tem_name=database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(da)).child(uid.key()).child('chd_name').get().val()
                tem_input=database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(da)).child(uid.key()).child('input time').get().val()
                print(tem_input)
                tem_people=database.child('register').child(str(this_year)+'-'+str(this_month)+'-'+str(da)).child(uid.key()).child('people').get().val()
                if input_t1[da] =='':
                    order1[da]=tem_name+'('+str(tem_people)+')'
                    input_t1[da]=tem_input
                else:
                    if input_t1[da]>tem_input:
                        print(input_t1[da]>tem_input)
                        if iinput_t2[da] =='':
                            order2[da]=order1[da]
                            input_t2[da]=input_t1[da]
                            
                            order1[da]=tem_name+'('+tem_people+')'
                            input_t1[da]=tem_input
                        else:
                            if input_t2[da] >tem_input:
                                print(input_t2[da] >tem_input)
                               
                                order2[da]=tem_name+'('+tem_people+')'
                                input_t2[da]=tem_input
                    else:
                        if input_t2[da] =='':
                            order1[da]=tem_name+'('+tem_people+')'
                            input_t1[da]=tem_input
                        else:
                            if input_t2[da] >tem_input:
                                print(input_t2[da] >tem_input)
                               
                                order2[da]=tem_name+'('+tem_people+')'
                                input_t2[da]=tem_input


        except:
            pass
    '''
                   
    #lists=zip(this_month_date,order1,order2)
    this,or1,or2=ordering()
    lists=zip(this,or1,or2)
    print(lists)
    #except:
    #    pass    
    print(this_month)
    #print(this_month_date)
    #print(name)
    return render(request,'welcome.html',{'e':email,'lists':lists,'this_month':this_month})

def logout(request):
    try:
        del request.session['uid']
    except KeyyError:
        pass

    return render(request,'signIn.html')

def signUp(request):

    return render(request,'signup.html')

def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get("pass")
    chd_name=request.POST.get("chd_name")
    phone_num=request.POST.get("phone_num")
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        message="unable to create account try again"
        return render(request,'signup.html',{'mssg':message})
    uid=user['localId']

    data={'name':name,'status':'1','chd_name':chd_name,'phone_num':phone_num}
    database.child('users').child(uid).child("details").set(data)
    return render(request,'signIn.html')

def create(request):

    return render(request,'create.html')

def post_create(request):

    import time
    from datetime import datetime, timezone
    import pytz

    tz= pytz.timezone('Asia/Seoul')
    time_now= datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili"+str(millis))
    date = request.POST.get('date')
    people =request.POST.get('people')
    try:
        idtoken= request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print(a)
        name = database.child('users').child(a).child('details').child('name').get().val()
        chd_name=database.child('users').child(a).child('details').child('chd_name').get().val()
        print("info"+str(a))
        if database.child('register').child(date).get().key()==a:
            message='이미 등록 되어 있는 날짜입니다.'
            return render(request,'create.html', {'msg':message})
        data = {
            "name":name,
            'chd_name':chd_name,
            'people':people,
            'input time':millis,
            'state':0,
        }
        database.child('register').child(date).child(a).set(data)
        
        this,or1,or2=ordering()
        lists=zip(this,or1,or2)

        return render(request,'welcome.html', {'e':name,'lists':lists,'this_month':this_month})
    except KeyError:
        message="Oops! User Logged Out Please SignIn Again"
        return render(request,'signup.html',{'mssg':message})

def check(request):
    import datetime
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    timestamps = database.child('users').child(a).child('reports').shallow().get().val()
    
    lis_time=[]
    for i in timestamps:

        lis_time.append(i)

    lis_time.sort(reverse=True)
    print('list')
    print(lis_time)
    work = []

    for i in lis_time:

        wor=database.child('users').child(a).child('reports').child(i).child('work').get().val()
        work.append(wor)
    print('work')
    print(work)

    date=[]
    for i in lis_time:
        i = float(i)
        print('date')
        print(int(datetime.datetime.fromtimestamp(i).strftime('%m')))
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date.append(dat)
    print('date')
    print(date)

    comb_lis = zip(lis_time,date,work)
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request,'check.html',{'comb_lis':comb_lis,'e':name})

def post_check(request):

    import datetime

    time = request.GET.get('z')

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    work =database.child('users').child(a).child('reports').child(time).child('work').get().val()
    progress =database.child('users').child(a).child('reports').child(time).child('progress').get().val()
    i = float(time)
    dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request,'post_check.html',{'w':work,'p':progress,'d':dat,'e':name})



