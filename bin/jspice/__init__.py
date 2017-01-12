#!/usr/bin/python
#############################################################
#             /######            /##                        #
#            /##__  ##          |__/                        #
#        /##| ##  \__/  /######  /##  /#######  /######     #
#       |__/|  ######  /##__  ##| ## /##_____/ /##__  ##    #
#        /## \____  ##| ##  \ ##| ##| ##      | ########    #
#       | ## /##  \ ##| ##  | ##| ##| ##      | ##_____/    #
#       | ##|  ######/| #######/| ##|  #######|  #######    #
#       | ## \______/ | ##____/ |__/ \_______/ \_______/    #
#  /##  | ##          | ##                                  #
# |  ######/          | ##                                  #
#  \______/           |__/                                  #
#							    #
#                 Jorge I. Zuluaga (C) 2016		    #
#############################################################
#Function: jSpice basic python routines
#############################################################

#############################################################
#EXTERNAL MODULES
#############################################################

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#SENSIBLE MODULES
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import sys,os,inspect,zmq,cgi,glob,signal

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#USEFUL MODULES
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import datetime

#############################################################
#MACROS
#############################################################
argv=sys.argv
stderr=sys.stderr
stdout=sys.stdout
exit=sys.exit

#############################################################
#UTIL ROUTINES
#############################################################
def loadConf(path):
    conf=dict()
    execfile(path+"/server.cfg",{},conf)
    return conf

def logEntry(flog,entry,instance="root"):
    time=datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S")
    log="[%s] [%s] %s\n"%(time,instance,entry)
    flog.write(log)
    flog.flush()
    #print>>stderr,log,
