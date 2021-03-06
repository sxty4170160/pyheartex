from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='pyheartex',
    version='0.0.7',
    description='Deploying machine learning for Heartex or Label Studio',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/heartexlabs/pyheartex',
    author='Heartex',
    author_email='hello@heartex.ai',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Flask==1.0.2',
        'attrs==19.1.0',
        'rq==1.0',
        'numpy>=1.16.3',
        'requests==2.22.0'
    ],
    python_requires='>=3.6',
)
