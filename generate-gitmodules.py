#!/usr/bin/python
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os

import requests
import yaml

TEMPLATE = """[submodule "%s"]
\tpath = %s
\turl = ../../%s.git
\tbranch = .
"""

# only return projects starting with openstack
CONFIG = ("https://opendev.org/openstack/governance/raw/reference/projects.yaml")


def find_integrated_gate_repos():
    r = requests.get(CONFIG)
    projects = yaml.safe_load(r.text)
    repos = []
    for project in projects.values():
        for deliverable in project.get('deliverables', {}).values():
            for repo in deliverable['repos']:
                repos.append(repo)
    return repos


def gen_gitmodules(projects):
    path_template = "https://opendev.org/{project}"
    short_projects = []
    for project in projects:
        short = os.path.basename(project)
        short_projects.append(short)
        path = path_template.format(project=project)
        if not os.path.isdir(short):
            os.system('git submodule add {path}'.format(path=path))
    for existing in os.listdir('.'):
        if not os.path.isdir(existing) or existing.startswith('.'):
            continue
        if existing not in short_projects:
            os.system('git rm {existing}'.format(existing=existing))
    projects = sorted(projects)
    with open(".gitmodules", 'w') as f:
        for p in projects:
            ns, name = p.split('/')
            f.write(TEMPLATE % (name, name, p))


def main():
    repos = find_integrated_gate_repos()
    gen_gitmodules(repos)


if __name__ == '__main__':
    main()
