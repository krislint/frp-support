from subprocess import Popen, PIPE
import time
from log import getLogger



logger = getLogger("frp")

RUN_FRP_CMDS = ['D:\\frp_0.36.2_windows_386\\frpc.exe','-c','D:\\frp_0.36.2_windows_386\\frpc.ini']



def run_frp():
    running_proc = Popen(RUN_FRP_CMDS, stdout=PIPE, stderr=PIPE,shell = True)
    
    while True:
        retcode = running_proc.poll()
        if retcode is not None:
            logger.error(running_proc.stderr.readlines(10))
            logger.error(retcode)
            break
        line = ""
        while line := running_proc.stdout.readline():
            # print(line)
            logger.info(line)
        time.sleep(10)
    try:
        running_proc.kill()
    except Exception as e:
        logger.error(e)

if __name__ =="__main__":
    run_frp();