from setuptools import setup, find_packages

setup(name='donkeypart_tub',
      version='0.1.1',
      description='JSON based datastore for the donkeycar.',
      long_description="no long description given",
      long_description_content_type="text/markdown",
      url='https://github.com/autorope/donkeypart_tub',
      author='Will Roscoe',
      author_email='wroscoe@gmail.com',
      license='MIT',
      entry_points={
          'console_scripts': [
              'donkey=donkeycar.management.base:execute_from_command_line',
          ],
      },
      install_requires=['numpy',
                        'pillow',
                        'docopt',
                        'tornado==4.5.3',
                        'h5py',
                        'pandas',
                        ],

      extras_require={'dev': ['pytest-cov']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='selfdriving cars donkeycar diyrobocars datastore',
      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      )
