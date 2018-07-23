# -*- coding: utf-8 -*-
# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import os.path

from setuptools import setup, find_packages

from dist_utils import fetch_requirements
from dist_utils import apply_vagrant_workaround
from dist_utils import get_version_string

ST2_COMPONENT = 'st2common'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(BASE_DIR, 'requirements.txt')
INIT_FILE = os.path.join(BASE_DIR, 'st2common/__init__.py')

install_reqs, dep_links = fetch_requirements(REQUIREMENTS_FILE)

apply_vagrant_workaround()
setup(
    name=ST2_COMPONENT,
    version=get_version_string(INIT_FILE),
    description='{} StackStorm event-driven automation platform component'.format(ST2_COMPONENT),
    author='StackStorm',
    author_email='info@stackstorm.com',
    license='Apache License (2.0)',
    url='https://stackstorm.com/',
    install_requires=install_reqs,
    dependency_links=dep_links,
    test_suite=ST2_COMPONENT,
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['setuptools', 'tests']),
    scripts=[
        'bin/st2-bootstrap-rmq',
        'bin/st2-cleanup-db',
        'bin/st2-register-content',
        'bin/st2-apply-rbac-definitions',
        'bin/st2-purge-executions',
        'bin/st2-purge-trigger-instances',
        'bin/st2-run-pack-tests',
        'bin/st2ctl',
        'bin/st2-generate-symmetric-crypto-key',
        'bin/migrations/v1.5/st2-migrate-datastore-to-include-scope-secret.py',
        'bin/migrations/v2.1/st2-migrate-datastore-scopes.py',
        'bin/migrations/v2.1/st2-migrate-runners.sh',
        'bin/st2-self-check',
        'bin/st2-track-result',
        'bin/st2-validate-pack-config',
        'bin/st2-check-license',
        'bin/st2-pack-install'
    ],
    entry_points={
        'st2common.metrics.driver': [
            'statsd = st2common.metrics.drivers.statsd_driver:StatsdDriver',
            'noop = st2common.metrics.drivers.noop_driver:NoopDriver',
        ],
    }
)
