from setuptools import setup, find_packages

setup(
    name='subzero',
    version='0.1',
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'scikit-learn'],
    author='Joseph Ogunfowokan',
    author_email='josephoguns5@gmail.com',
    description='A machine learning framework',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/joecode77/subzero',
)
