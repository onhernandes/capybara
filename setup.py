from distutils.core import setup

setup(
    name="Capybara",
    version="1.0.0",
    author="Matheus Hernandes",
    author_email="midia.matheus@gmail.com",
    scripts=["main.py"],
    license="LICENSE",
    description="Twitter bot for posting photos",
    long_description=open("README.md").read(),
    install_requires=[
        "PyYAML == 5.4",
        "mongoengine == 0.15.3",
        "twitter == 1.18.0"
    ],
)

