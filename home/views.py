import json
from django.http import HttpResponse
from django.shortcuts import render
from home.models import User
from celery import schedules
from djcelery.models import (PeriodicTask, IntervalSchedule, CrontabSchedule)



def index(request):
    if request.method == 'POST':
        if 'schedule' in request.POST:
            
            # get the values from the form
            number = request.POST.get('phonenum')
            zipcode = request.POST.get('zipcode')
            sendtime = request.POST.get('sendtime')
            sendtime = sendtime.split(':')
            
            user = User.objects.filter(phoneNumber=number)
            if user:
                return render(request, 'home/signuperror.html')
            
            # add the job to the scheduler
            schedule = CrontabSchedule(hour=sendtime[0],minute=sendtime[1])
            schedule.save()
            arguments = json.dumps({"number":number,"zipcode":zipcode})
            modelData = dict(
                name=number,
                task="home.tasks.send",
                crontab_id=schedule.pk,
                kwargs=arguments,
            )
            periodicTask = PeriodicTask(**modelData)
            periodicTask.save()
            newUser = User(phoneNumber=number,zipCode=zipcode,sendTime=(sendtime[0] + sendtime[1]),cronjobID=schedule.pk)
            newUser.save()
            # try:
            #     periodicTask.save()
            # except:
            #     from django.db import connection
            #     print connection.queries
            #     raise
            return render(request, 'home/thanks.html')
            
        elif "remove" in request.POST:
            number = request.POST.get('phonenum')
            user = User.objects.filter(phoneNumber=number)
            if not user:
                return render(request, 'home/removeerror.html')
            CrontabSchedule.objects.get(pk=user[0].cronjobID).delete()
            user.delete()
            return render(request, 'home/goodbye.html')
            
        
    return render(request, 'home/index.html')