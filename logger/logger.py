import yaml
import logging.config

LOG_CONFIG = "logger/log_config.yml"
def setup_logger():
    with open (LOG_CONFIG, "r") as file:
        config = yaml.load(file, Loader=yaml.UnsafeLoader)

    logging.config.dictConfig(config)
    