#!/usr/bin/env python
"""
Script to generate alton and git commands for executing hotfixes
Commands for:
  - cutting amis
  - creating hotfix tag

The script should be run with the hotfix's git hash as a command-line argument.
Otherwise, the script will prompt the user for the hotfix hash.
i.e. `python scripts/hotfix.py <hotfix hash>`
"""
import datetime
import sys

if len(sys.argv) == 2:
    hotfix_hash = sys.argv[1]
else:
    hotfix_hash = raw_input("Please enter hotfix's git hash: ")

print ""
print "Here are the alton commands to cut the hotfix amis:"
print """
@alton cut ami for stage-edx-edxapp from prod-edx-edxapp with edx_platform_version={hotfix_hash}
@alton cut ami for prod-edge-edxapp from prod-edge-edxapp with edx_platform_version={hotfix_hash}
@alton cut ami for prod-edx-edxapp from prod-edx-edxapp with edx_platform_version={hotfix_hash}
""".strip().format(hotfix_hash=hotfix_hash)


git_string = datetime.datetime.today().strftime(
    'git tag -a hotfix-%Y-%m-%d -m "Hotfix for %b %d, %Y" {hotfix_hash}'
).format(hotfix_hash=hotfix_hash)

print "\nHere is the git command to generate the hotfix tag:"
print git_string
print "Once you run that command, push the tag by running:"
print "git push --tags"
