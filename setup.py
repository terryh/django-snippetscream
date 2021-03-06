from setuptools import setup, find_packages
from setuptools.command.test import test

def run_tests(self):
    from setuptest.runtests import runtests
    return runtests(self)
test.run_tests = run_tests

setup(
    name='django-snippetscream',
    version='0.0.6',
    description='Django app packaging the best snippets found on http://djangosnippets.org',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Shaun Sephton',
    author_email='shaunsephton@gmail.com',
    url='http://github.com/shaunsephton/django-snippetscream',
    packages=find_packages(),
    include_package_data=True,
    test_suite="snippetscream.tests",
    tests_require=[
        'django-setuptest',
    ],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
