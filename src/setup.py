import setuptools

import setuptools

setuptools.setup(
    name                            = "myorquestra",
    packages                        = setuptools.find_packages(where = "python"),
    package_dir                     = {
        "" : "python"
    },
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)

# setuptools.setup(
#     name="welcome-resource",
#     version="0.1.0",
#     py_modules=['myorquestra']
# )

# setuptools.setup(
#     name="orquestra",
#     version="0.1",
#     packages=setuptools.find_packages(),
# )