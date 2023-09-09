import pathlib
import yaml


class Config:
    def __init__(self, path: str = "config/config.yaml"):
        BASE_DIR = pathlib.Path(__file__).parent.parent
        self.config_path = BASE_DIR / path

    def config(self,):
        with open(self.config_path) as f:
            config = yaml.safe_load(f)
        return config
