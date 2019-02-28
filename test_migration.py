from Migration import Migration


config = {
    "name": "test_migration",
    "reco_file_name": "/scratch3/lwilkins/Data/OutputNtuples_2.4.42_Dec18/ljets_ge4jge1b1smt/ttbar_PP8AFII_m170_Dec18_nominal.root",
    "reco_tree_name": "nominal",
    "truth_file_name": "file",
    "truth_tree_name": "tree",
}
migration = Migration("test_migration", config)

print("hello")
