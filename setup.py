import pathlib
from setuptools import setup

readme_file = pathlib.Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name="energyplus_python_apps",
    version="22.2.0-Beta5",
    packages=['energyplus_python_apps'],
    description="Meta-package collecting all official EnergyPlus Python utilities",
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Edwin Lee, for NREL, for United States Department of Energy',
    author_email='a@a.a',
    url='https://github.com/Myoldmopar/EnergyPlusPythonApps',
    license='UnlicensedForNow',
    install_requires=[
        'energyplus-launch==3.5.3',
        'energyplus-ruleset-model==0.2',
        'energyplus-transition-tools==2.0.3',
        'energyplus-pet==0.43',
        'energyplus-idd-idf-utilities==0.86',
        'energyplus-regressions==1.9.7',
        'energyplus-api-helpers==0.2',
    ]
)
