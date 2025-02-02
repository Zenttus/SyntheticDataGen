import json
import glob


class Configuration:

    def __init__(self, path=None):
        if path is None:
            self.conf = dict()
        else:
            with open(path) as f:
                self.conf = json.load(f)

    def add_settings(self, path_to_results="./results", res_x=640, res_y=480, label="xml", images_per_background=5):
        self.conf['SETTINGS'] = {}
        self.conf['SETTINGS']['PathToResults'] = path_to_results
        self.conf['SETTINGS']['ResX'] = res_x
        self.conf['SETTINGS']['ResY'] = res_y
        self.conf['SETTINGS']['LabelType'] = label
        self.conf['SETTINGS']["imagesPerBackground"] = images_per_background

    def add_actor(self, path, label, size=[1.0, 1.0, 1.0]):
        if "ACTORS" not in self.conf:
            self.conf["ACTORS"] = {}

        obj = dict()
        obj["id"] = len(self.conf["ACTORS"])
        obj["path"] = path
        obj["label"] = label
        obj["size"] = size

        self.conf["ACTORS"][label] = obj

    def add_panel(self, path, objects, image_size, size_ranges, rotation_ranges, max_objects, lamp_position_range, lamp_color):
        if "PANELS" not in self.conf:
            self.conf["PANELS"] = []

        background = dict()
        background["id"] = len(self.conf["PANELS"])
        background["path"] = path
        background["objects"] = objects
        background["size"] = image_size
        background["objectsSizeRanges"] = size_ranges
        background["rotations"] = rotation_ranges
        background["maxObjects"] = max_objects
        background["lampPositionRange"] = lamp_position_range
        background["lampColor"] = lamp_color

        self.conf["PANELS"].append(background)

    # TODO def add_mask()

    def add_backgrounds_from_directory(self, path, objects, image_size, size_ranges, rotation_ranges, max_objects, lamp_position_range, lamp_color):
        if "BACKGROUNDS" not in self.conf:
            self.conf["BACKGROUNDS"] = []

        for file in glob.glob(path):  # TODO multiple images types
            self.add_panel(file, objects, image_size, size_ranges, rotation_ranges, max_objects, lamp_position_range, lamp_color)

    def save_conf_to_file(self, path='config.json'):
        json_string = json.dumps(self.conf)

        with open(path, 'w') as f:
            f.write(json_string)

    #  TODO def get_color_from_image(self):
