#!/bin/bash

echo "Current directory, in which hdf5 will be cloned: $PWD"

HDF5_BRANCH=${HDF5_BRANCH:-develop}
HDF5_URL=${HDF5_URL:-"https://github.com/HDFGroup/hdf5.git"}

if [ ! -d hdf5 ]; then
  git clone --recurse-submodules --single-branch --depth 1 --shallow-submodules ${HDF5_URL} -b ${HDF5_BRANCH}
fi

cd hdf5/test
mkdir -p build
cd build
cmake ..
make -j$($(nproc)/2) # To speed up building hdf5
ctest -j $($(nproc)/2) # To speed up testing hdf5

ret = $?
return ret