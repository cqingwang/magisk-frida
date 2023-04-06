import re
import requests
import subprocess
import config


# 12.7.5-2, 12.7.5-3, ... -> 12.7.5
def strip_revision(tag) -> str:
    return tag.split('-', 1)[0]


def release_by(versions, target_version):
    if target_version is not None:
        for v in versions:
            if v["tag_name"] == target_version:
                return v
    return versions[0]


# gets last tag of GitHub project
def get_target_github_tag(project_name, target_version=None) -> str:
    # releases_url = f"https://api.github.com/repos/{project_name}/releases/latest"
    releases_url = f"https://api.github.com/repos/{project_name}/releases"
    all_releases = requests.get(releases_url, headers=config.auth_headers).json()
    releases = release_by(all_releases, target_version)
    # TODO: don't assume order
    last_release = releases["tag_name"]
    return last_release


# gets last tag of frida
def get_target_frida_tag(target_version=None) -> str:
    last_frida_tag = get_target_github_tag('hzzheyang/strongR-frida-android', target_version)
    print(f"target frida tag: {last_frida_tag}")
    return last_frida_tag


# properly sort tags (e.g. 1.11 > 1.9)
def sort_tags(tags: [str]) -> [str]:
    tags = tags.copy()
    s: str
    tags.sort(key=lambda s: list(map(int, re.split(r"[\.-]", s))))
    return tags
