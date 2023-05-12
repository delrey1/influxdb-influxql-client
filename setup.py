from setuptools import setup, find_packages  # noqa: H301

requires = [
    'setuptools >= 21.0.0',
    'requests >= 2.28.2',
    'pydantic'
]

NAME = "influxql_client"

setup(
    name=NAME,
    version='0.0.1',
    description="InfluxDB InfluxQL Basic Library",
    keywords=["InfluxDB", "InfluxDB Python Client", "InfluxQL"],
    install_requires=requires,
    packages=find_packages(exclude=('tests*',)),
    test_suite='tests',
    python_requires='>=3.7',
    include_package_data=True,
    classifiers=[
    ])
