from Migration import Migration
from array import array

config = {
    "name": "test_migration",
    "reco_file_name": "/scratch3/lwilkins/Data/OutputNtuples_2.4.42_Dec18/ljets_ge4jge1b1smt/ttbar_PP8AFII_m170_Dec18_nominal.root",
    "reco_tree_name": "nominal",
    "truth_file_name": "/scratch3/lwilkins/Data/OutputNtuples_2.4.42_Dec18/ljets_ge4jge1b1smt/ttbar_PP8AFII_m170_Dec18_nominal.root",
    "truth_tree_name": "nominal",
    "reco_binning": array("d", [1, 2, 3, 4]),
    "truth_binning": array("d", [1, 2, 3, 4]),
}


migration = Migration("test_migration", config)

print("Complete")
