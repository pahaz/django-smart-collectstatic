|version|

|pyversions| |license|

**Author**: `Pahaz Blinov`_

**Repo**: https://github.com/pahaz/django-smart-collectstatic/

Micro fix Django manage.py collectstatic command.

This fix uses COPY and LINK strategy for collecting static files.

If the static file in `settings.BASE_DIR` it will be linked. 
In other case it will be coppied.

It tested only on Django 1.9, 1.10 and Python 3.4, 3.5

Installation
============

`django-smart-collectstatic`_ is on PyPI, so simply run:

::

    pip install django-smart-collectstatic

or ::

    easy_install django-smart-collectstatic

to have it installed in your environment.

For installing from source, clone the
`repo <https://github.com/pahaz/django-smart-collectstatic>`_ and run::

    python setup.py install

If you don`t have **pip** you can `install it <https://pip.pypa.io/en/stable/installing/#installation>`_

Typical use case
================

I use it inside a Docker container. For callectiong Django static.

Dockerfile::

    ...
    RUN python3 manage.py smartcollectstatic --noinput --link
    ...


.. _Pahaz Blinov: https://github.com/pahaz/
.. _django-smart-collectstatic: https://pypi.python.org/pypi/django-smart-collectstatic
.. |DwnMonth| image:: https://img.shields.io/pypi/dm/django-smart-collectstatic.svg
.. |DwnWeek| image:: https://img.shields.io/pypi/dw/django-smart-collectstatic.svg
.. |DwnDay| image:: https://img.shields.io/pypi/dd/django-smart-collectstatic.svg
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/django-smart-collectstatic.svg
.. |version| image:: https://img.shields.io/pypi/v/django-smart-collectstatic.svg
   :target: `django-smart-collectstatic`_
.. |license| image::  https://img.shields.io/pypi/l/django-smart-collectstatic.svg
   :target: https://github.com/pahaz/django-smart-collectstatic/blob/master/LICENSE
