# Copyright 2018 Max Shinn <max@maxshinnpotential.com>
# 
# This file is part of Paranoid Scientist, and is available under the
# MIT license.  Please see LICENSE.txt in the root directory for more
# information.

from . import decorators

def accepts(*argtypes, **kwargtypes):
    return lambda f: f

def returns(returntype):
    return lambda f: f
            
def requires(condition):
    return lambda f: f

def ensures(condition):
    return lambda f: f

def immutable_argument(func):
    return func

def paranoidclass(cls):
    return cls

decorators.accepts = accepts
decorators.returns = returns
decorators.requires = requires
decorators.ensures = ensures
decorators.immutable_argument = immutable_argument
decorators.paranoidclass = paranoidclass
