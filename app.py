import argparse
from yaml import load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from cleaner import Cleaner


DEFAULT_CONFIG_FILE = 'config.yaml'


def create_config():
    config = {}
    with open(DEFAULT_CONFIG_FILE, 'r') as stream:
        config = load(stream, Loader=Loader)
    return config


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--noop", action="store_true", help="boolean; if set, will only print what it would have done.")
    parser.add_argument("--pages", type=int, help="integer; the maximum number of pages to get from the Slack API")
    return parser.parse_args() 


def main():
    config = create_config()
    args = parse_args()
    cleaner = Cleaner(config, args)
    cleaner.clean()


if __name__ == "__main__":
    main()

