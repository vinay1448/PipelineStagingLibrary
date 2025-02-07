Pipeline Staging in a Sales Management System

A Web Application intended for customers or clients from contrasting domains seeking to upskill business outcomes with the supplementary contribution of 'Pipeline Stages'. This is a demonstration intended to prioritize the the Customer - Key Priority relationship in a cloud-ready environment.

Custom Libraries for PipelineStagingLibrary:
- setuptools 69.5.1
- wheel 0.43.0
- twine 5.0.0

**setup.py:** custom-pipeline-stages-manager 0.1.0

Custom Packages for AWS S3 Facilitation:
- boto3 1.34.88
- s3transfer 0.10.1
- botocore 1.34.88

**Library**:

Hierarchy and Structure:

```bash
PipelineStagingLibrary
              -------> .git
              -------> _dist
              -------> dist
              -------> env
              -------> pipeline_staging_properties_pkg
		              ----> __init__.py
		              ----> pipeline_staging_properties.py
              -------> pkg_newfinalcustom_pipeline_staging_final.egg-info
              -------> tests
              -------> CHANGELOG.txt
              -------> LICENSE
              -------> README.md
              -------> setup.py
```

Build the library i.e. generate the distribution package:

```bash
  python3 -m pip install --upgrade setuptools wheel
```

Upload/publish the distribution package files with twine:

```bash
  python3 -m pip install --upgrade twine
```

Publish the library to PyPI:

```bash
  python3 -m twine upload --repository pypi dist/*
  twine upload dist/*
```
Install (i.e. via pip) the distribution package/library:

```bash
  python3 -m pip install --index-url https://pypi.org/simple --no-deps custom-pipeline-stages-manager==0.1.0
```
Information about the installed library:

```bash
  pip list
  pip show custom-pipeline-stages-manager
```

## Configuration Files

- setup.py
Metadata of Custom Library :
```bash
 custom-pipeline-stages-manager 
 version=0.1.0
```