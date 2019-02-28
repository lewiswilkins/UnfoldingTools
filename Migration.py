import ROOT as r


class Migration(object):
    def __init__(self, name, config):
        r.gErrorIgnoreLevel = r.kFatal
        self.name = name
        self.config = config
        self._check_config(self.config)
        self.reco_file = self._get_file(config["reco_file_name"])
        self.reco_tree = self._get_tree(self.reco_file, config["reco_tree_name"])
        self.truth_file = self._get_file(config["truth_file_name"])
        self.truth_tree = self._get_tree(self.truth_file, config["truth_tree_name"])

    def _get_tree(self, file, tree_name):
        tree = file.Get(tree_name)
        if self._check_tree_exists(file, tree_name):
            return tree
        else:
            print(
                "Migration::Error: {0} does not exist inside {1}. Please add a real tree.".format(
                    tree_name, file.GetName()
                )
            )
            exit()

    def _get_file(self, file_name):
        file = r.TFile(file_name, "READ")
        if file.IsZombie():
            print(
                "Migration::Error: {0} does not exist. Please add a real file.".format(
                    file_name
                )
            )
            exit()
        return file

    def _check_config(self, config):
        required_keys = [
            "reco_file_name",
            "reco_tree_name",
            "truth_file_name",
            "truth_tree_name",
        ]
        missing_keys = False
        for key in required_keys:
            try:
                config[key]
            except KeyError:
                print(
                    "Migration::Error: Missing {0} in config. Please add and re-run.".format(
                        key
                    )
                )
                missing_keys = True

        if missing_keys:
            exit()

    def _check_tree_exists(self, file, tree_name):
        if file.GetListOfKeys().Contains(tree_name):
            return True
