import configparser
import importlib
import logging


def get_cloud_handler(config_path='/etc/smartscheduler/config.cfg'):
    config = configparser.RawConfigParser()
    config.read(config_path)
    module = importlib.import_module(config.get('cloud', 'driver'))
    cloud_handler = module.init_handler(dict(config.items('cloud')))
    return cloud_handler


def get_monitoring_handler(config_path='/etc/smartscheduler/config.cfg'):
    config = configparser.ConfigParser()
    config.read(config_path)
    module = importlib.import_module(config.get('monitoring', 'driver'))
    dbms_handler = module.init_handler(dict(config.items('monitoring')))
    return dbms_handler


def init_logging(config_path='/etc/smartscheduler/config.cfg'):
    config = configparser.ConfigParser()
    config.read(config_path)
    logger = logging.getLogger(config.get('logging', 'name'))
    logger.setLevel(logging.getLevelName(config.get('logging', 'level')))
    handler = logging.FileHandler(config.get('logging', 'filename'))
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
