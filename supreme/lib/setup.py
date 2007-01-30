def configuration(parent_package='', top_path=None, package_name='lib'):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(package_name,parent_package,top_path)
    config.add_subpackage('klt')
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(configuration=configuration)
