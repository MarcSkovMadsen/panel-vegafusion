"""Here we import the different task submodules/ collections"""
from invoke import Collection

from . import build, test

# pylint: disable=invalid-name
# as invoke only recognizes lower case
namespace = Collection()
namespace.add_collection(build)
namespace.add_collection(test)
