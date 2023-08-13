import os
import argparse
import yaml
import logging

def read_params(config_path):
    with open (config_path, 'r') as f:
        config=yaml.safe_load(f)
    return config


def main(config_path,datasource):
    config=read_params(config_path)
    print(config)


if  __name__=='__main__':
    args=argparse.ArgumentParser()
    default_config_path=os.path.join("config", "params.yaml") # it helps to avoid os command differences
    args.add_argument('--config',default=default_config_path)
    args.add_argument('--datasource',default=None)

    parsed_args=args.parse_args()
    # print(parsed_args.config,parsed_args.datasource)
    main(config_path=parsed_args.config,datasource=parsed_args.datasource)

