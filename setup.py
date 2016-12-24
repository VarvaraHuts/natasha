from setuptools import (
    Command,
    setup,
    find_packages,
)
from natasha import (
    __version__,
    BUILD_DEFAULT_PIPELINES,
)


class BuildDictionariesCommand(Command):

    user_options = []

    def initialize_options(self):
        self.pipelines = BUILD_DEFAULT_PIPELINES()

    def finalize_options(self):
        pass

    def run(self):
        print('=> Building pipeline dictionaries ...')
        for pipeline in self.pipelines:
            print('Building', pipeline.__class__.__name__, '...')
            pipeline.build()


setup(
    name='natasha',
    version=__version__,
    description='Named-entity recognition for russian language',
    url='https://github.com/bureaucratic-labs/natasha',
    author='Dmitry Veselov',
    author_email='d.a.veselov@yandex.ru',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic',
    ],
    cmdclass={
        'build_dicts': BuildDictionariesCommand,
    },
    package_data = {
        'natasha.grammars': [
            'dictionaries/*.dawg',
        ],
    },
    keywords='natural language processing, russian morphology, named entity recognition, tomita',
    packages=find_packages(),
    install_requires=[
        'yargy==0.5.2'
    ],
)
