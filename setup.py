from setuptools import setup

setup(
    name='Flask-Shop',
    version='1.0.0',
    packages=['flask_shop'],
    include_package_data=True,
    url='https://github.com/sangjiexun/Flask-Shop',
    license='MIT',
    author='Flask Shop Team',
    author_email='',
    description='A Flask-based e-commerce website',
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Security',
        'Flask-Mail',
        'Flask-Babel',
        'Flask-Uploads',
        'Pillow',
    ],
)
