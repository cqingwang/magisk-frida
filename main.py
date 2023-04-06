#!/user/bin/env python3
#
# MagiskFrida build process
#
# 1. Checks if project has a tag that matches frida tag
#    Yes -> continue
#    No  -> must tag
# 2. Checks if last commit doesn't have frida tag and is titled 'release'
#    Yes -> must tag
#    No  -> continue
# If tagging, writes new tag to 'NEW_TAG.txt' and builds
# Otherwise, does nothing and builds with placeholder tag
# 3. Deployment will execute only if 'NEW_TAG.txt' is present
#
# NOTE: Requires git
#

import build
import config
import util


def main():
    latest_version = util.get_target_frida_tag()
    build.do_build(latest_version, '0')

    for target_version in config.target_versions:
        build.do_build(target_version, '0')


if __name__ == "__main__":
    main()
