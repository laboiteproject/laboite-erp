La Boite ERP
============

|travis| |master-coverage|

.. |travis| image:: https://travis-ci.org/laboiteproject/laboite-erp.svg?branch=master
    :target: https://travis-ci.org/laboiteproject/laboite-erp

.. |readthedocs| image:: https://readthedocs.org/projects/kinto/badge/?version=latest
    :target: https://kinto.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |master-coverage| image::
    https://coveralls.io/repos/laboiteproject/laboite-erp/badge.svg?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/laboiteproject/laboite-erp

.. |pypi| image:: https://img.shields.io/pypi/v/kinto.svg
    :target: https://pypi.python.org/pypi/kinto


La Boite ERP is a Django project to handle stock and accounting for the project.

* `Issue tracker <https://github.com/laboiteproject/laboite-erp/issues>`_

Install and run
---------------

::

   mkvirtualenv .venv
   source .venv/bin/activate
   pip install django
   ./manage.py migrate
   ./manage.py runserver


Requirements
------------

* **Python**: 3.5+
