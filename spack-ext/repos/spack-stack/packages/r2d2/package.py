# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class R2d2(PythonPackage):
    """Research Repository for Data and Diagnostics (R2D2) for JEDI at JCSDA."""

    homepage = "https://github.com/JCSDA-internal/r2d2-client"
    git = "https://github.com/JCSDA-internal/r2d2-client.git"
    url = "https://github.com/JCSDA-internal/r2d2-client/archive/refs/heads/feature/restapi.zip"

    maintainers("climbfuji", "ericlingerfelt")

    version("restapi", branch="feature/restapi", no_cache=True)

    depends_on("python@3.9:", type=("run"))
    depends_on("py-pyyaml", type=("run"))
    depends_on("py-boto3", type=("run"))
    depends_on("py-charset-normalizer", type=("run"))
    depends_on("py-idna", type=("run"))
    depends_on("py-requests", type=("run"))
    depends_on("py-s3transfer", type=("run"))
    depends_on("py-setuptools", type=("build", "run"))
