import requests
import os
# import urllib.parse

def get_text(filename):
    with open(filename) as f:
        text = f.read()
    return text

# def get_section(text, start, finish):
#     description_string = sections[start]
#     index = text.find(description_string)
#     if index > -1:
#         start_index = index + len(description_string)
#     else:
#         raise Exception(f"Could not find {description_string}")
#
#     key_features_string = sections[finish]
#     index_end = text.find(key_features_string)
#     if index_end < 0:
#         raise Exception(f"Could not find {key_features_string}")
#
#     return text[start_index: index_end]

def check_spelling(text):
    endpoint = "http://api.grammarbot.io/v2/check"
    parameters = {
        "api-key": "KS9C5N3Y",
        "language": "en-US",
        "text": text
    }

    results = requests.post(endpoint, params=parameters)

    results.raise_for_status()

    json_results = results.json()
    matches = json_results.get("matches", [])

    if len(matches) == 0:
        return []

    for match in matches:
        offset = match.get('offset')
        length = match.get('length')
        replacement = match.get('replacements')[0].get('value') if len(match.get('replacements')) else ""
        print("")
        print(f"{match.get('message')}")
        print(f"Context: {match.get('sentence')}")
        print(f"Original Text: {text[offset: (offset + length)]}")
        print(f"Suggested Change: {replacement}")

    return matches

# sections = {
#     "description": "# Description",
#     "key_features": "# Key Features",
#     "requirements": "# Requirements",
#     "documentation": "# Documentation",
#     "setup": "## Setup",
#     "usage": "### Usage",
#     "technical_details": "## Technical Details",
#     "troubleshooting": "## Troubleshooting",
#     "version_history": "# Version History",
#     "links": "# Links",
#     "references": "## References"
# }

def fix_known_errors(text):
    stuff_to_remove = [
        "_"
        "IPs",
        "geo-location",
        "IPStack",
        "Whois",
        "WHOIS",
        "pan",
        "OS",
        "phishy",
        "Datetime",
        "insightidr",
        "ldap",
        "JIRA",
        "remediations",
        "JQL",
        "@Security",
        "permalink"
    ]

    for stuff in stuff_to_remove:
        text = text.replace(stuff,"")

    return text


def spell_check_help_md(help_md_file):
    filename = help_md_file.split("/")[-1]
    help_text = get_text(help_md_file)

    # description = get_section(help_text, "description", "key_features")
    # key_features = get_section(help_text, "key_features", "requirements")

    print(f"checking: {help_md_file}")
    help_text = fix_known_errors(help_text)
    check_spelling(help_text)

dirs = os.listdir("../workflows/")
print(dirs)
bad_dirs = [".DS_Store"]

for dir in dirs:
    if not dir in bad_dirs:
        filepath = f"../workflows/{dir}/help.md"
        spell_check_help_md(filepath)

# spell_check_help_md("../workflows/Delete_O365_Emails_With_Slack/help.md")
