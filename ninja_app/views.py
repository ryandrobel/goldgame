from django.shortcuts import render, redirect
import random


def index(request):    
    if "gold_created" in request.session:
        request.session['counter'] = request.session['counter'] + request.session['gold_created']
    else:
        request.session['counter'] = 0
        request.session['gold_created'] = 0
        request.session['activity_log'] = ''

    return render(request, "index.html")

def process_money(request):
    if request.POST['money_box'] == 'farm':
        request.session['gold_created'] = random.randint(10, 20)
        request.session['activity_log'] = f"Gold earned farm. Farmer ass ma-fuc...{request.session['gold_created']}"
    if request.POST['money_box'] == 'cave':
        request.session['gold_created'] = random.randint(5, 10)
        request.session['activity_log'] = f"Gold earned cave. Can I have some!?{request.session['gold_created']}"
    if request.POST['money_box'] == 'house':
        request.session['gold_created'] = random.randint(2, 5)
        request.session['activity_log'] = f"Gold earned house. From my freaking house!?{request.session['gold_created']}"
    if request.POST['money_box'] == 'casino':
        request.session['gold_created'] = random.randint(-50, 50)
        if request.session['gold_created'] > 0:
            request.session['activity_log'] = f"Gold earned casino. Stop taking my gold{request.session['gold_created']}"
        else:
            request.session['activity_log'] = f"Gold lost casino. That sucks hahaha{request.session['gold_created']}"

    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect('/')