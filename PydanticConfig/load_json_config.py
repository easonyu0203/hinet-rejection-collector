from .config_model import Config
from pathlib import Path
import json


def load_json_config(config_file_path: Path) -> Config:
    """
    load config form a json file to config pydantic object,
    return Config loaded with config data
    :param config_file_path: json file
    :return: Config pydantic object
    """
    with open(config_file_path) as f:
        data = json.load(f)
    return Config.parse_obj(data)


config_file: Path = Path(__file__).parent.parent / 'config.json'
config = load_json_config(config_file)
