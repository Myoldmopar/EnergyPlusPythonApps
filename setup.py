import pathlib
from setuptools import setup

from energyplus_python_apps import NAME, VERSION

readme_file = pathlib.Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name=NAME,
    version=VERSION,
    packages=['energyplus_python_apps'],
    description="Meta-package collecting all official EnergyPlus Python utilities",
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Edwin Lee, for NREL, for United States Department of Energy',
    author_email='a@a.a',
    url='https://github.com/Myoldmopar/EnergyPlusPythonApps',
    license='UnlicensedForNow',
    install_requires=[
        'energyplus-launch==3.5.7',
        'energyplus-ruleset-model==0.4',
        'energyplus-transition-tools==2.0.6',
        'energyplus-pet==0.48',
        'energyplus-idd-idf-utilities==0.87',
        'energyplus-regressions==2.0.2',
        'energyplus-api-helpers==0.3',
        'energyplus-diff-analysis==0.2',
        # 'energyplus-expand-objects==blah',
        # 'energyplus-epjson-editor==blah',
    ],
    entry_points={
        'console_scripts': [
            'energyplus_python_configure=energyplus_python_apps.configure:configure_cli',
        ]
    }
)
