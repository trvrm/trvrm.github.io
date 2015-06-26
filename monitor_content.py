#!/usr/bin/env python3
print('wtf')

import watchdog,time,os, io
from watchdog.observers import Observer
from subprocess import check_call,check_output
import logging
import sys
assert sys.version_info.major==3



LOGFILE_PATH= '/tmp/monitor_blog.log'
logging.basicConfig(filename=LOGFILE_PATH,level=logging.DEBUG,format='%(asctime)s: %(filename)s:%(lineno)d:%(levelname)s:%(message)s',)
logging.getLogger().setLevel(logging.DEBUG)


THIS_DIRECTORY      = os.path.abspath(os.path.dirname(__file__))
CONTENT_DIRECTORY   = os.path.join(THIS_DIRECTORY,'_content')
 
def build():
    print('build')
    logging.info("build")
    os.chdir(THIS_DIRECTORY)
    cmd=['fab','build']
    try:
        out=check_output(cmd)
        logging.info(out)
    except Exception as e:
        logging.exception(e)
    print(out)
    
class MyHandler(watchdog.events.FileSystemEventHandler):
   def on_created(self,event):
       print(event.src_path)
       build()
   def on_modified(self,event):
       print(event.src_path)
       build()
   
       
       
if __name__=='__main__':       
    print('main')
    logging.info("main")
    observer=Observer()
    observer.schedule(MyHandler(),CONTENT_DIRECTORY)
    
    observer.start()
    
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


