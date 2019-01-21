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


def main():
    config = create_config()
    cleaner = Cleaner(config)
    cleaner.clean()


if __name__ == "__main__":
    main()

