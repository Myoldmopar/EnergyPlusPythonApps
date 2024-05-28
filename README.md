# EnergyPlus Python Apps

This is a meta-project which simply depends on all the EnergyPlus "Official" Python utilities.
This project itself does not create any new utilities, or contain any code.
This really just pins the dependencies at specific versions and ensures compatability in the installation dependencies.

## Releases

[![DevelopmentTest](https://github.com/Myoldmopar/EnergyPlusPythonApps/actions/workflows/test.yml/badge.svg)](https://github.com/Myoldmopar/EnergyPlusPythonApps/actions/workflows/test.yml)
[![PyPIRelease](https://github.com/Myoldmopar/EnergyPlusPythonApps/actions/workflows/release.yml/badge.svg)](https://github.com/Myoldmopar/EnergyPlusPythonApps/actions/workflows/release.yml)

I think long term, this "project" itself will be tagged with versions in sync with EnergyPlus itself.
To install all EnergyPlus Python utilities, simply execute, for example,  `pip install energyplus_python_apps==22.2.0`.

## Current Repos

This project is currently linking to the following packages:

| PyPi Project Name            | Project Description                                                                  | Repository                                                   |
|------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------|
| energyplus-launch            | A graphical interface and workflow manager for EnergyPlus                            | https://github.com/NREL/EP-Launch                            |
| energyplus-ruleset-model     | A utility for generating ruleset model reports from EnergyPlus inputs and outputs    | https://github.com/jasonglazer/createrulesetmodeldescription |
| energyplus-transition-tools  | A lightweight interface for automatically transitioning EnergyPlus input files       | https://github.com/Myoldmopar/EnergyPlusTransitionTools      |
| energyplus-pet               | A library and graphical tool for generating input coefficients for EnergyPlus models | https://github.com/Myoldmopar/energypluspet                  |
| energyplus-idd-idf-utilities | A lightweight library for processing and querying idd and idf files                  | https://github.com/Myoldmopar/py-idd-idf                     |
| energyplus-regressions       | A tool for comparing results from two EnergyPlus builds, for E+ developer usage      | https://github.com/NREL/EnergyPlusRegressionTool             |
| energyplus-api-helpers       | A set of helper classes and demos for interacting with the EnergyPlus API            | https://github.com/Myoldmopar/EnergyPlusAPIHelper            |
| energyplus-diff-analysis     | Tools for plotting and comparing csv data from two separate EnergyPlus runs          | https://github.com/mitchute/energyplus-diff-analysis         |
| energyplus-version           | Python-based version update classes and utilities                                    | https://github.com/mitchute/energyplus-version               |

## Usage

Cover a few topics here:
 - Installation
 - Running the configuration script after install
 - Accessing all the tools, including the dev tools
 - Updating