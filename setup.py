from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ez',
      version=version,
      description="The ez Web Framework",
      long_description="""\
A simple and compact yet powerful web framework for Google AppEngine.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='web framework google appengine',
      author='John Evans',
      author_email='john@jpevans.com',
      url='http://www.jpevans.com/software/ez',
      license='LICENSE',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          "PasteScript>=1.3"
      ],
      package_data = {
        'ez':['pro']
      },
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      ez = ez.templates:EzProjectTemplate
      """,
      )
