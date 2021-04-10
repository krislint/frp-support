
import time
from start_frp import run_frp
from net_util import check_connect,doConnectionChange

from log import logger
import _thread

configMap ={
    "host" : "gg.lolitahub.cn",
    "port" : "443"
}

def main():
    logger.info("frp support started")

    _thread.start_new_thread(run_frp,())
    logger.info(" frp started")


    logger.info("start check network")

    while True:
        result = check_connect(**configMap)

        if not result:
            doConnectionChange()
            time.sleep(30)
            check_connect(**configMap)

        time.sleep(30)
        


if __name__ == '__main__':
    main()