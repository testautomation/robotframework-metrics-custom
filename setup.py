from setuptools import setup, find_packages

filename = 'robotframework_metrics_custom/version.py'
exec(compile(open(filename, 'rb').read(), filename, 'exec'))

setup(name='robotframework-metrics-custom',
      version=__version__,
      description='Custom metrics based report for robot framework',
      long_description='Custom metrics based report for robot framework',
      classifiers=[
          'Framework :: Robot Framework',
          'Programming Language :: Python',
          'Topic :: Software Development :: Testing',
      ],
      keywords='robotframework report',
      author='Shiva Prasad Adirala',
      author_email='adiralashiva8@gmail.com',
      url='https://github.com/adiralashiva8/robotframework-metrics-custom',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'robotframework',
          'beautifulsoup4',
          'gevent'
      ],
      entry_points={
          'console_scripts': [
              'robotcmetrics=robotframework_metrics_custom.runner:main',
          ]
      },
      )
