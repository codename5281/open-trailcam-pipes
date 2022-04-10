from setuptools import setup, find_packages
import os


def parse_requirements(file):
    return sorted(set(
        line.partition('#')[0].strip()
        for line in open(os.path.join(os.path.dirname(__file__), file))
    ) - set(''))


setup(
	name='open-trailcam-pipes',
	python_requires='>=3.9.6',
	description='Open Trailcam Pipes',
	version = '0.1',
	author='Jérémy LAVARENNE (@codename5281)',
	packages=find_packages(where='src'),
	install_requires=parse_requirements('requirements.txt'),
	package_dir={'': 'src'}
	)