#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': '',
 'author_email': '',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': "'OpenMDAO drivers using DAKOTA (Design Analysis Kit for Optimization and Terascale Applications)'",
 'download_url': '',
 'entry_points': '[openmdao.component]\ndakota_driver.test.test_driver.VectorStudy=dakota_driver.test.test_driver:VectorStudy\ndakota_driver.driver.DakotaVectorStudy=dakota_driver.driver:DakotaVectorStudy\ndakota_driver.driver.DakotaCONMIN=dakota_driver.driver:DakotaCONMIN\ndakota_driver.test.test_driver.ConstrainedOptimization=dakota_driver.test.test_driver:ConstrainedOptimization\ndakota_driver.test.test_driver.Textbook=dakota_driver.test.test_driver:Textbook\ndakota_driver.test.test_driver.ParameterStudy=dakota_driver.test.test_driver:ParameterStudy\ndakota_driver.test.test_driver.SensitivityStudy=dakota_driver.test.test_driver:SensitivityStudy\ndakota_driver.driver.DakotaBase=dakota_driver.driver:DakotaBase\ndakota_driver.test.test_driver.Optimization=dakota_driver.test.test_driver:Optimization\ndakota_driver.test.test_driver.Rosenbrock=dakota_driver.test.test_driver:Rosenbrock\ndakota_driver.driver.DakotaGlobalSAStudy=dakota_driver.driver:DakotaGlobalSAStudy\ndakota_driver.driver.DakotaOptimizer=dakota_driver.driver:DakotaOptimizer\ndakota_driver.test.test_driver.Broken=dakota_driver.test.test_driver:Broken\ndakota_driver.driver.DakotaMultidimStudy=dakota_driver.driver:DakotaMultidimStudy\n\n[openmdao.driver]\ndakota_driver.driver.DakotaOptimizer=dakota_driver.driver:DakotaOptimizer\ndakota_driver.driver.DakotaVectorStudy=dakota_driver.driver:DakotaVectorStudy\ndakota_driver.driver.DakotaCONMIN=dakota_driver.driver:DakotaCONMIN\ndakota_driver.driver.DakotaBase=dakota_driver.driver:DakotaBase\ndakota_driver.driver.DakotaGlobalSAStudy=dakota_driver.driver:DakotaGlobalSAStudy\ndakota_driver.driver.DakotaMultidimStudy=dakota_driver.driver:DakotaMultidimStudy\n\n[openmdao.container]\ndakota_driver.driver.DakotaOptimizer=dakota_driver.driver:DakotaOptimizer\ndakota_driver.driver.DakotaVectorStudy=dakota_driver.driver:DakotaVectorStudy\ndakota_driver.driver.DakotaCONMIN=dakota_driver.driver:DakotaCONMIN\ndakota_driver.test.test_driver.ConstrainedOptimization=dakota_driver.test.test_driver:ConstrainedOptimization\ndakota_driver.test.test_driver.VectorStudy=dakota_driver.test.test_driver:VectorStudy\ndakota_driver.test.test_driver.SensitivityStudy=dakota_driver.test.test_driver:SensitivityStudy\ndakota_driver.driver.DakotaBase=dakota_driver.driver:DakotaBase\ndakota_driver.test.test_driver.Optimization=dakota_driver.test.test_driver:Optimization\ndakota_driver.driver.DakotaGlobalSAStudy=dakota_driver.driver:DakotaGlobalSAStudy\ndakota_driver.test.test_driver.Rosenbrock=dakota_driver.test.test_driver:Rosenbrock\ndakota_driver.test.test_driver.Textbook=dakota_driver.test.test_driver:Textbook\ndakota_driver.test.test_driver.ParameterStudy=dakota_driver.test.test_driver:ParameterStudy\ndakota_driver.test.test_driver.Broken=dakota_driver.test.test_driver:Broken\ndakota_driver.driver.DakotaMultidimStudy=dakota_driver.driver:DakotaMultidimStudy',
 'include_package_data': True,
 'install_requires': ['openmdao.main', 'pyDAKOTA'],
 'keywords': ['openmdao'],
 'license': 'Apache License, Version 2.0',
 'maintainer': '',
 'maintainer_email': '',
 'name': 'dakota_driver',
 'package_data': {'dakota_driver': ['sphinx_build/html/index.html',
                                    'sphinx_build/html/.buildinfo',
                                    'sphinx_build/html/py-modindex.html',
                                    'sphinx_build/html/objects.inv',
                                    'sphinx_build/html/searchindex.js',
                                    'sphinx_build/html/search.html',
                                    'sphinx_build/html/pkgdocs.html',
                                    'sphinx_build/html/usage.html',
                                    'sphinx_build/html/genindex.html',
                                    'sphinx_build/html/srcdocs.html',
                                    'sphinx_build/html/_sources/usage.txt',
                                    'sphinx_build/html/_sources/pkgdocs.txt',
                                    'sphinx_build/html/_sources/index.txt',
                                    'sphinx_build/html/_sources/srcdocs.txt',
                                    'sphinx_build/html/_static/plus.png',
                                    'sphinx_build/html/_static/comment-bright.png',
                                    'sphinx_build/html/_static/comment.png',
                                    'sphinx_build/html/_static/down-pressed.png',
                                    'sphinx_build/html/_static/sidebar.js',
                                    'sphinx_build/html/_static/doctools.js',
                                    'sphinx_build/html/_static/ajax-loader.gif',
                                    'sphinx_build/html/_static/default.css',
                                    'sphinx_build/html/_static/down.png',
                                    'sphinx_build/html/_static/jquery.js',
                                    'sphinx_build/html/_static/underscore.js',
                                    'sphinx_build/html/_static/minus.png',
                                    'sphinx_build/html/_static/up-pressed.png',
                                    'sphinx_build/html/_static/up.png',
                                    'sphinx_build/html/_static/pygments.css',
                                    'sphinx_build/html/_static/searchtools.js',
                                    'sphinx_build/html/_static/file.png',
                                    'sphinx_build/html/_static/basic.css',
                                    'sphinx_build/html/_static/websupport.js',
                                    'sphinx_build/html/_static/comment-close.png',
                                    'sphinx_build/html/_modules/index.html',
                                    'sphinx_build/html/_modules/dakota_driver/driver.html',
                                    'sphinx_build/html/_modules/dakota_driver/test/test_driver.html',
                                    'test/__init__.py',
                                    'test/openmdao_log.txt',
                                    'test/test_driver.py']},
 'package_dir': {'': 'src'},
 'packages': ['dakota_driver', 'dakota_driver.test'],
 'url': 'https://github.com/OpenMDAO-Plugins/dakota_driver',
 'version': '0.4',
 'zip_safe': False}


setup(**kwargs)

