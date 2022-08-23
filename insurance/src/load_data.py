from distutils.command.config import config
import os
import yaml
import pandas as pd
import argparse
from pkgutil import get_data
import configparser



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args=args.parse_args()
    data=get_data(config_path=parsed_args.config)