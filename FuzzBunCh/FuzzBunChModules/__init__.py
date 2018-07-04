import os
import sys
import importlib
import System


# OpenTions
FB='MandySa'





def LoadModules(NAME):
	try:
		LoadModule=importlib.import_module(NAME)
	except ImportError:
		print '['+System.print_red('!')+']Module call fails, or the file doesn\'t exist\n'
	else:
		print '['+System.print_green('+')+']The call is successful\n'
		ModulesCommand(NAME,LoadModule)
def ModulesInfo(Message,List,Pm,Plist):
	
	print '['+System.print_blue('*')+']See the module information\n---------------------------------------------------------------------------------------'
	Par=Pm
	Len=len(Plist)
	print 'Options Infromatcion--------------------------------------------------- '
	for i in range(Len):
		LIST_NAME=Plist[i]
		Name_Type=Pm[LIST_NAME]
		print '     '+System.print_purple(LIST_NAME)+'='+System.print_yellow(Name_Type)
	print System.print_red('======================================================================')




	MessageLen=len(List)
	for index in range(MessageLen):
		ListName=List[index]
		NameType=Message[ListName]
		print '            '+System.print_red(ListName)+':'+System.print_blue(NameType)
	print '---------------------------------------------------------------------------------------'
#end
def ModulesCommand(Modules,import_Modules):
	Modules_Class=import_Modules.FuzzBunChModules
	while -1:
                Command=raw_input(System.print_red(FB)+'  '+System.print_blue(Modules)+' >')
                if Command=='exit' or Command=='quit' or Command=='exit()':
                        print ' ['+System.print_green("*")+']Exit The Modules\n\n'
		elif Command.split(' ')[0]=='set':		
			if len(Command.split(' '))==3:
				NAME=Command.split(' ')[1]
				Type=Command.split(' ')[2]
				if NAME in Modules_Class.parameter:
					Modules_Class.parameter[NAME]=Type
					print '['+System.print_green('+')+']Modify the parameters successfully\n'+'	'+NAME+'============>'+System.print_green(Type)+'\n\n'
				else:
					print '['+'!'+']Parameter does not exist'
			elif len(Command.split(' '))==2:
				print '['+System.print_red('!')+']Please enter a value\n'
			elif len(Command.split(' '))==1:
                                print '['+System.print_red('!')+']Parameter name does not exist\n'
		elif Command=='exploit' or Command=='run':
			import_Modules.Exploit(Modules_Class.parameter)
		elif Command=='info':
			Mess=Modules_Class.Message
			ModulesInfo(Mess,Modules_Class.MessageList,Modules_Class.parameter,Modules_Class.parameterList)
		elif Command.split(' ')[0]=='show':
			if len(Command.split(' '))==2:
                        	SHOW_NAME=Command.split(' ')[1]
				
				if SHOW_NAME in Modules_Class.parameter:
					print '['+System.print_green('+')+']Check the parameters\n'
					print ' 	'+SHOW_NAME+'============'+System.print_red(Modules_Class.parameter[SHOW_NAME])+'\n'

				elif SHOW_NAME=='payload' or SHOW_NAME=='Payload':
					print '==============================================================='
					print 'Php/Shell/Reverse    :TCP Shell Reverse Php  '
		elif Command=='show':		
			print '['+System.print_red('!')+']Please input parameters\nhelp Options Payload'	
					













def KernelSetSettion(Parameter_Name,Text):
	Class = LoadModule.FuzzBunChModules
	try:
		Settion=Class.parameter
	except:
		print '['+System.print_red("!")+']Please select the module!]\n'
	else:
		try:
			Settion[Parameter_Name]=Text
		except:
			print '['+System.print_red('!')+']There is no parameter\n'
		else:
			print '['+System.print_green('+')+']Modify the success\n'
			print '			'+Parameter_Name+' ===> '+Text
