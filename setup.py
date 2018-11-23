from setuptools import setup
package_name = 'py_symlink_install_test'
setup(
    name=package_name,
    version='1.0.0',
    install_requires=['setuptools'],
    package_dir={'': 'src'},
    packages=[package_name],
    scripts=['scripts/entry'],
    zip_safe=True
)
