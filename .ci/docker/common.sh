#!/bin/bash
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

set -ex

# shellcheck source=/dev/null
as_ci_user() {
  # NB: unsetting the environment variables works around a conda bug
  #     https://github.com/conda/conda/issues/6576
  # NB: Pass on PATH and LD_LIBRARY_PATH to sudo invocation
  # NB: This must be run from a directory that the user has access to
  sudo -E -H -u ci-user env -u SUDO_UID -u SUDO_GID -u SUDO_COMMAND -u SUDO_USER env "PATH=${PATH}" "LD_LIBRARY_PATH=${LD_LIBRARY_PATH}" "$@"
}

pip_install() {
  as_ci_user conda run -n "py_${PYTHON_VERSION}" pip install --progress-bar off "$@"
}

install_pip_dependencies() {
  pushd /opt/conda
  # Install all Python dependencies, including PyTorch
  pip_install -r /opt/conda/requirements.txt
  pip_install --pre torch --index-url https://download.pytorch.org/whl/nightly/cpu
  popd
}

install_pip_dependencies
