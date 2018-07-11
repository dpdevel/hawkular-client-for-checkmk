from setuptools import setup

_VERSION = '0.18.4'
_DESCRIPTION = 'Read/Write data to and from a Hawkular metric server.'

setup(name='hawkular-client-for-checkmk',
    version=_VERSION,
    description='Hawkular client cli fof ChecMK output',
    long_description=_DESCRIPTION,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Monitoring',
    ],
    url='http://github.com/dpdevel/hawkular-client-for-checkmk',
    author='Domenico Pastore',
    author_email='domenico.pastore93@gmail.com',
    license='Apache License 2.0',
    packages=['hawkular_client_for_checkmk'],
    install_requires=[
        'future>=0.15.0',
        'python-dateutil>=2.0.0',
        'PyYAML>=3.0',
        'hawkular-client>=0.5.2',
    ],
    entry_points={
        'console_scripts': ['hawkular-cli=hawkular_client_cli.command_line:main'],
    },
    include_package_data=True,
    zip_safe=False)
