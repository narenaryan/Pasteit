import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

#Added additional requirements
requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'mysql-python',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    ]

setup(name='listing',
      version='0.0',
      description='listing',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Naren Arya',
      author_email='narenarya@live.com',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='listing',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = listing:main
      [console_scripts]
      initialize_listing_db = listing.scripts.initializedb:main
      """,
      )
