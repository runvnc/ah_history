from setuptools import setup, find_packages

setup(
    name="ah_history",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    include_package_data=True,
    package_data={
        'ah_history': [
            'static/js/*.js',
            'inject/*.jinja2',
        ],
    },
    install_requires=[
        "fastapi"
    ],
)
