from setuptools import setup

setup(
    name = 'mltoolkit',
    version = '0.7.2',    

    description = 'A useful toolkit for working with machine learning models',
    url = 'https://github.com/flimao/mltoolkit',
    author = 'LmnICE',
    author_email = 'mltoolkit@dev.lmnice.me',
    license = 'GNU GPLv3',
    packages = ['mltoolkit'],
    install_requires = [
        'numpy', 'pandas', 'typing', 'scikit-learn', 'matplotlib', 'seaborn', 
        'scipy', 'six', 'pmdarima', 'unidecode', 'gensim'
    ],

    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Machine Learning',
        'License :: OSI Approved :: GNU GPLv3',         
        'Programming Language :: Python :: 3',
    ],
)
