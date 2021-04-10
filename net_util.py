import socket
from log import getLogger
from subprocess import Popen
logger = getLogger("net process")


def check_connect(host,port,timeout=20):

    connect = None
    try:
        connect = socket.create_connection((host,port),timeout=timeout)
    except Exception as e:
        logger.error("connect socket error")
        return False
    finally:
        if connect != None:
            try:
                connect.close()
            except Exception as e:
                logger.error("connect socker close error")
    logger.info("connect success")
    return True


def doConnectionChange():
    logger.info("start network change")

    import os
    rs = os.system('''powershell -c start -verb runas  E:\project\\frp-support\\net.cmd ''');
    logger.info(rs)
    logger.info("network change end")




if __name__ =='__main__':
    check_connect('gg.lolitahub.cn',443)