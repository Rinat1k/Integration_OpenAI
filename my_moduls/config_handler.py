import json


class ConfigHandler:
    def __init__(self, config_path='configs/api_keys.json'):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            return config
        except FileNotFoundError:
            print(f"Config file not found. Creating a new one at {self.config_path}.")
            return {}

    def get_value(self, keys, default=None):
        current_level = self.config
        for key in keys:
            current_level = current_level.get(key, {})
        return current_level if current_level else default
