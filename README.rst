OpenStack
=========

OpenStack is a collection of interoperable components that can be deployed
to provide computing, networking and storage resources. Those infrastructure
resources can then be accessed by end users through programmable APIs.

This repository just represents OpenStack as a collection of git submodules.
You can find the repositories for individual components at:
https://opendev.org/openstack

You can learn more about the various components in OpenStack at:
https://openstack.org/software

To learn more about how to contribute to OpenStack, please head to our
Contributor portal: https://www.openstack.org/community/

To learn more about how OpenStack is governed, you can visit:
https://governance.openstack.org/


Why this repository ?
---------------------

Our continuous integration system, Zuul, gates all of the contained projects
in an effective single timeline. This means that OpenStack, across all of the
projects, does already have a sequence of combinations that have been
explicitly tested, but it's non-trivial to go from a single commit of a
particular project to the commits that were tested with it.

Gerrit's submodule tracking feature will update a super project every
time a subproject is updated, so the specific sequence created by zuul
will be captured by the super project commits.

This repo is intended to be used in a read-only manner. Any commit in this
repo will get a collection of commits in the other repos that have
explicitly been tested with each other, if that sort of thing is important
to you.
