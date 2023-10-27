[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[project]
name = "pyflowqc"
authors = [{name = "Simone Puccio", email = "simone.puccio@cnr.it", role = "Maintainer"}]
readme = "README.md"
dynamic = ["version"]
description = "PyFlowQC is a Python package for flow and mass cytometry quality control."
requires-python = '>= 3.9'
dependencies = [
    "numpy",
    "pandas",
    "anndata",
    "scanpy",
    "scipy",
    "seaborn",
    "matplotlib",
    "readfcs >=1.1.0",
    "datashader"
]

[project.urls]
Home = "https://github.com/luglilab/PyFlowQC"

# [project.optional-dependencies]
# dev = [
#     "pre-commit",
#     "nox",
#     "lndocs==0.2.0",
# ]
# test = [
#     "pytest>=6.0",
#     "pytest-cov",
#     "nbproject_test >= 0.2.0",
# ]

[tool.black]
preview = true

# [tool.pytest.ini_options]
# testpaths = [
#     "tests",
#     "docs/tutorials",
# ]

[tool.coverage.run]
omit = [
    "PyFlowQC/*",
]