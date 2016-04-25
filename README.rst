OpenStack Tracking Repo
=======================

Zuul gates all of the contained projects in an effective single timeline. This means that OpenStack, across all of the projects, does
already have a sequence of combinations that have been explicitly tested, but it's non-trivial to go from a single commit of a particular
project to the commits that were tested with it.

Gerrit's submodule tracking feature will update a super project every time a subproject is updated, so the specific sequence created by
Zuul will be captured by the super project commits.

This repo is intended to be used in a read-only manner. Any commit in this repo will get a collection of commits in the other repos that
have explicitly been tested with each other, if that sort of thing is important to you.
