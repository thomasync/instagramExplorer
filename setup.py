from setuptools import setup, find_packages
setup(
    name = 'instagramExplorer',
    packages = find_packages(),
    package_data={'': ['headers.json']},
    include_package_data=True,
)