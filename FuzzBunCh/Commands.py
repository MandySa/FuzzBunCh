# -*- coding: utf-8 -*
import System
import os
import sys
import importlib
import FuzzBunChModules
import readline



#Options Message
FB='MandySa'
Modules='WICMB'
Email='1026111251@qq.com'
Webst='www.nsa.gov'  #zhuangbi
Organ='National Security Agency and Central Intelligence Agency'
sys.path.append('/FuzzBunCh/FuzzBunCh/FuzzBunChModules')
def Bannder():
	os.system('clear')
	print System.print_green('                                                                      \n                                                                      \n                                                                      \n                                                                      \n                                                                      \n                                                                      \n  ##      ##     o# ####      #####   ###         ##    #####r        \n  ##     ###     ##  ##    ##         ####       #/#    #    N#       \n   ##    # ##   N#   ##   ##          ## #      ##V#    #     #       \n    #   ## o#   ##   ##  .#V          ##  #    ## V#    #####         \n    ## /#   ## o#    ##   ##          ##  N#  ##  V#    #     ##      \n     # #!    # #V    ##   ##          ##   ##.#   V#    #     ##      \n     ###     ###    ####    ###  ###  ##    ##    V#    #######       \n                                                                      \n                                                                      \n                                                                      \n                                                                      \n                                                                      \n                                                                      ')
	print System.print_blue('Shell')+System.print_red('Author information\n')
	print '     Copyright: '+System.print_blue('Mandy Sa and Michael Rogers') +'  Email: '+System.print_purple(Email)+'\n'
	print '     Website: '+System.print_blue(Webst)+'   Team: '+System.print_green('Bald Eagle Sea Safety Team')+'\n'

	print '     Organization: '+System.print_yellow(Organ)+'\n'





def OpenModules(NAME):	
	FuzzBunChModules.LoadModules(NAME)

def Commands():
	Bannder()
	print '['+System.print_green('INFO')+']'+'Profile information is complete'
	while -1:
		Command=raw_input(System.print_red(FB)+'  '+System.print_blue(Modules)+' >')
		if Command=='exit' or Command=='quit' or Command=='exit()':
			print ' ['+System.print_green("*")+']Exit the program\n\n'
			break
			exit()
		elif Command=='help' or Command=='help()':
                        print System.print_red('Author information\n')
                        print '     Copyright: '+System.print_blue('Mandy Sa and Michael Rogers') +'  Email: '+System.print_purple(Email)+'\n'
                        print '     Website: '+System.print_blue(Webst)+'   Team: '+System.print_green('Bald Eagle Sea Safety Team')+'\n'
                        print '     Organization: '+System.print_yellow(Organ)+'\n'
		elif Command.split(' ')[0]=='use':
			UseModulesName=Command.split(' ')[1]
			print '['+System.print_blue('*')+']Open Modules Name:'+System.print_red(UseModulesName)
			OpenModules(UseModulesName)
#		elif Command.split(' ')[0]=='set':
#			print '['+System.print_blue('*')+']Modify the parameters'
#			SetSettion(Command.split(' ')[1],Command.split(' ')[2])
			






























































		else:
			print '['+System.print_red('!')+']Please input the correct'
		














