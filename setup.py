from distutils.core import setup

pluginPkgs = []
pluginPkgs.append('stamp.plugins')
pluginPkgs.append('stamp.plugins.common')
pluginPkgs.append('stamp.plugins.common.multipleComparisonCorrections')
pluginPkgs.append('stamp.plugins.groups')
pluginPkgs.append('stamp.plugins.groups.effectSizeFilters')
pluginPkgs.append('stamp.plugins.groups.plots')
pluginPkgs.append('stamp.plugins.groups.plots.configGUI')
pluginPkgs.append('stamp.plugins.groups.statisticalTests')
pluginPkgs.append('stamp.plugins.multiGroups')
pluginPkgs.append('stamp.plugins.multiGroups.effectSizeFilters')
pluginPkgs.append('stamp.plugins.multiGroups.plots')
pluginPkgs.append('stamp.plugins.multiGroups.plots.configGUI')
pluginPkgs.append('stamp.plugins.multiGroups.postHoc')
pluginPkgs.append('stamp.plugins.multiGroups.statisticalTests')
pluginPkgs.append('stamp.plugins.samples')
pluginPkgs.append('stamp.plugins.samples.effectSizeFilters')
pluginPkgs.append('stamp.plugins.samples.plots')
pluginPkgs.append('stamp.plugins.samples.plots.configGUI')
pluginPkgs.append('stamp.plugins.samples.statisticalTests')
pluginPkgs.append('stamp.plugins.samples.confidenceIntervalMethods')

metagenomicPkgs = []
metagenomicPkgs.append('stamp.metagenomics')
metagenomicPkgs.append('stamp.metagenomics.fileIO')
metagenomicPkgs.append('stamp.metagenomics.simulations')
metagenomicPkgs.append('stamp.metagenomics.stats')
metagenomicPkgs.append('stamp.metagenomics.stats.CI')
metagenomicPkgs.append('stamp.metagenomics.stats.distributions')
metagenomicPkgs.append('stamp.metagenomics.stats.empiricalTests')
metagenomicPkgs.append('stamp.metagenomics.stats.tests')

setup(
    name='STAMP',
    version='2.0.3',
    author='Donovan Parks, Rob Beiko',
    author_email='donovan.parks@gmail.com',
    packages=['stamp', 'stamp.GUI'] + pluginPkgs + metagenomicPkgs,
    package_data={'stamp': ['data/*.txt']},
    scripts=['bin/STAMP'],
    url='http://pypi.python.org/pypi/stamp/',
    license='GPL3',
    description='A graphical software package for analyzing taxonomic and functional profiles.',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy >= 1.7.1",
        "scipy >= 0.13.0",
        "matplotlib >= 1.3.1",
        "biom-format >= 1.2.0",
        "pyqi >= 0.2.0",],
)