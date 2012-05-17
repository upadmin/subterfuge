import os
    #Django Web Modules
from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.template import RequestContext
    #Database Models
from subterfuge.main.models import credentials
from subterfuge.modules.models import *
    #Additional Views
from subterfuge.cease.views import *
from subterfuge.modules.views import *


def globalvars():
   # Read in subterfuge.conf and Establish Global Variables
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
      conf = file.readlines()
      
   iface    = conf[15]
   gate     = conf[17]
   autoconf = conf[20]
   msfdir   = conf[34]


   # Subterfuge Module Builder
def build(request, modname):

      #Create Module Directory
   os.system('mkdir modules/' + modname + '/')

   #Build Appropriate .mod files
   #Add Module to plugins.ext


   # Subterfuge Module Builder
def create(request):

      #Module Name
   modname     = str(request.POST['modname'])

      #Create Module Space
   build(request, modname)
      
      #Get/Write Files
   if request.FILES['modicon']:
      icon = request.FILES['modicon']
      dest = open('templates/images/plugins/' + modname + '.png', 'wb+')
      for chunk in icon.chunks():
         dest.write(chunk)
      dest.close()
      
   try:
      guipage = request.FILES['guipage']
      dest = open('templates/mods/' + modname + '_page.mod', 'wb+')
      for chunk in  guipage.chunks():
         dest.write(chunk)
      dest.close()
   except:
      print "No GUI Page"
      
      
   if request.FILES['exploitcode']:
      exploitcode = request.FILES['exploitcode']
      dest = open('modules/' + modname + '/' + modname + '.py', 'wb+')
      for chunk in exploitcode.chunks():
         dest.write(chunk)
      dest.close()
   
      try:
         guisettings = request.FILES['guisettings']
         dest = open('templates/mods/' + modname + '_settings.mod', 'wb+')
         for chunk in guisettings.chunks():
            dest.write(chunk)
         dest.close()
      except:
         print "No GUI Settings"
      
      #Relay Template Variables
   return render_to_response("home.ext", {
	   "status"    :   "on",
   })


      #################################
      #Subterfuge Modules Section
      #################################
      
def builder(request): 
	   # Read in subterfuge.conf
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
      conf = file.readlines()
      
	   #Relay Template Variables
   return render_to_response("mod.ext", {
	   "conf"         :   str(conf[20]).rstrip('\n'),
	   "module_name"  :   request.META['PATH_INFO'].rstrip('/').strip('/'),
	   "module_page"  :   "mods/" + request.META['PATH_INFO'].rstrip('/').strip('/') + "_page.mod"
   })      
      
      
           
      #################################
      #HTTP CODE INJECTION MOD
      #################################

def httpcodeinjection(request, module, conf):
   # HTTP CODE INJECTION MODULE CONFIGURATION  
      # Status
   status = request.POST["status"]
      # Vector
   if request.POST["vector"]:
      exploit = request.POST["vector"] + "\n"
      method = "metasploit"
      # Payload
   if request.POST["payload"]:
      payload = request.POST["payload"] + "\n"
      
   if request.POST["custominject"]:
      exploit = ""
      payload = ""
      method = "custom"
         # Write Custom Inject into File
      with open(str(os.path.dirname(__file__)) + '/httpcodeinjection/inject.x', 'w') as file:
         file.writelines(request.POST["custominject"])
         
   installed.objects.filter(name = "httpcodeinjection").update(active = status)
   
   os.system('xterm -e sh -c "python ' + str(os.path.dirname(os.path.abspath(__file__))) + '/httpcodeinjection/httpcodeinjection.py ' + method + ' ' + payload + '" &')
   

   
      #################################
      #TUNNEL BLOCK MODULE
      #################################

def tunnelblock():
   os.system('python ' + str(os.path.dirname(os.path.abspath(__file__))) + '/TunnelBlock/TunnelBlock.py')

