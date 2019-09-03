import setuptools

from setuptools.command.develop import develop
from setuptools.command.install import install

#====================================================================#

#class PostDevelopCommand(develop):
#    """Post-installation for development mode."""
#    def run(self):
#        import LyaRT_Grid as LG
#        LG.Download_data( During_Installation=True )
#
#        develop.run(self)
#
#
#class PostInstallCommand(install):
#    """Post-installation for installation mode."""
#    def run(self):
#        import LyaRT_Grid as LG
#        LG.Download_data( During_Installation=True )

#        install.run(self)
#====================================================================#


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FLaREON",
    version="1.0.00",
    author="Siddhartha Gurung Lopez",
    author_email="sidgurung@cefca.es",
    description="Fast Lyman alpha Radiative Transfer for everyone!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sidgurun/LyaRT-Grid",
    packages=setuptools.find_packages(),
    #install_requires=[ 'sklearn>=20.0' ],
    install_requires=[ 'scikit-learn>=0.20.0' ],
    include_package_data = True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    #cmdclass={ 'develop': PostDevelopCommand,
    #           'install': PostInstallCommand, },
)

