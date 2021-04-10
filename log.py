import logging,logging.config,yaml

def initLog():
    with open(file="./log.yaml", mode='r', encoding="utf-8")as file:
        logging_yaml = yaml.load(stream=file, Loader=yaml.FullLoader)
        logging.config.dictConfig(config=logging_yaml)

initLog()

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.setLevel

def getLogger(name):
    log =  logging.getLogger(name)
    log.setLevel(logging.INFO)
    return log

