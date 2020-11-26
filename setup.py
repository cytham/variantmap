from setuptools import setup, find_packages
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

exec(open("variantmap/version.py").read())

setup(
    name='variantmap',
    version=__version__,
    packages=find_packages(),
    package_data={'variantmap.assets': ['*'],
                  'variantmap.data': ['*.h5']},
    include_package_data=True,
    url='https://github.com/cytham/variantmap',
    download_url='https://github.com/cytham/variantmap/releases',
    license='gpl-3.0',
    author='Tham Cheng Yong',
    author_email='chengyong.tham@u.nus.edu',
    description='Interactive heatmap for multi-sample structural variant analysis',
    keywords=['variantmap', 'structural variant', 'multiple samples', 'variantbreak', 'nanovar', 'heatmap'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pandas>=1.1.4', 'dash>=1.17.0', 'tables>=3.6.1'],
    python_requires='>=3.6',
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ]
)
