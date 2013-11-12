from setuptools import setup
from setuptools.command.test import test as TestCommand

import structpack


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '-x']
        self.test_suite = True

    def run_tests(self):
        import pytest
        raise SystemExit(pytest.main(self.test_args))


with open('README.md') as f:
    long_description = f.read()


setup(
    name='structpack',
    version=structpack.__version__,
    url='https://github.com/Knio/structpack',
    author='Tom Flanagan',
    author_email='tom@zkpq.ca',
    description='A Python library for serializing and deserializing object '
                'trees to JSON-compatable values (dicts, lists, strings, '
                'ints, floats, bools).',
    long_description=long_description,
    license='MIT',
    packages=['structpack'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    zip_safe=False,  # structpack is zip-safe, but i hate egg.
)
