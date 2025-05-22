# prompt: This looks like a great start to a GitHub issue template that includes both structured metadata and Python code snippets demonstrating interactive widgets and contact info. Here’s a clean, slightly improved version you could use directly as a .github/ISSUE_TEMPLATE/docs_update.yml (or .md) file, including:
# 	•	Clear section headers
# 	•	Instructions and placeholders for user input
# 	•	Your Python snippet (for Jupyter notebook use) with contact info printing
# ⸻
# ---
# name: Documentation
# about: Update or add documentation
# title: "[DOCS]: "
# labels: documentation, needs-triage
# ---
# Thanks for taking the time to fill this out! :bow:
# By submitting this issue, you agree to follow our [Code of Conduct](https://github.com/github/gh-copilot/blob/main/CODE_OF_CONDUCT.md).
# ### Describe the need
# _What do you wish was different about our docs?_
# ### Version
# _Do these docs apply to a specific version?_
# _Example: `gh-copilot v0.5.2-beta`_
# ### Relevant terminal output
# _Please copy and paste any relevant terminal output._
# _Please check your output before submission to ensure sensitive information is redacted._
# ---
# ```python
# import ipywidgets as widgets
# from IPython.display import display
# contact_info = {
#     "blank_issues_enabled": True,
#     "contact_links": [
#         {
#             "name": "Ask a question on how to use GitHub Copilot in the CLI",
#             "url": "https://github.com/github/gh-copilot/discussions",
#             "about": "For general-purpose questions and answers, see the Discussions section."
#         },
#         {
#             "name": "Ask a question about GitHub Copilot",
#             "url": "https://github.com/orgs/community/discussions/categories/copilot",
#             "about": "Please check out the GitHub community forum for discussions about GitHub Copilot."
#         },
#         {
#             "name": "GitHub Docs > GitHub Copilot in the CLI",
#             "url": "https://docs.github.com/en/copilot/github-copilot-in-the-cli",
#             "about": "For more information 

import ipywidgets as widgets
from IPython.display import display

contact_info = {
    "blank_issues_enabled": True,
    "contact_links": [
        {
            "name": "Ask a question on how to use GitHub Copilot in the CLI",
            "url": "https://github.com/github/gh-copilot/discussions",
            "about": "For general-purpose questions and answers, see the Discussions section."
        },
        {
            "name": "Ask a question about GitHub Copilot",
            "url": "https://github.com/orgs/community/discussions/categories/copilot",
            "about": "Please check out the GitHub community forum for discussions about GitHub Copilot."
        },
        {
            "name": "GitHub Docs > GitHub Copilot in the CLI",
            "url": "https://docs.github.com/en/copilot/github-copilot-in-the-cli",
            "about": "For more information about GitHub Copilot in the CLI."
        }
    ]
}

# Display contact info
for link in contact_info["contact_links"]:
    print(f"{link['name']}: {link['url']}")
    if 'about' in link:
        print(f"  - {link['about']}")
    print()
# prompt: Ask a question on how to use GitHub Copilot in the CLI: https://github.com/github/gh-copilot/discussions
#   - For general-purpose questions and answers, see the Discussions section.
# Ask a question about GitHub Copilot: https://github.com/orgs/community/discussions/categories/copilot
#   - Please check out the GitHub community forum for discussions about GitHub Copilot.
# GitHub Docs > GitHub Copilot in the CLI: https://docs.github.com/en/copilot/github-copilot-in-the-cli
#   - For more information about GitHub Copilot in the CLI.

import ipywidgets as widgets
from IPython.display import display


contact_info = {
    "blank_issues_enabled": True,
    "contact_links": [
        {
            "name": "Ask a question on how to use GitHub Copilot in the CLI",
            "url": "https://github.com/github/gh-copilot/discussions",
            "about": "For general-purpose questions and answers, see the Discussions section."
        },
        {
            "name": "Ask a question about GitHub Copilot",
            "url": "https://github.com/orgs/community/discussions/categories/copilot",
            "about": "Please check out the GitHub community forum for discussions about GitHub Copilot."
        },
        {
            "name": "GitHub Docs > GitHub Copilot in the CLI",
            "url": "https://docs.github.com/en/copilot/github-copilot-in-the-cli",
            "about": "For more information about GitHub Copilot in the CLI."
        }
    ]
}

# Create a dropdown widget
dropdown = widgets.Dropdown(
    options=[link["name"] for link in contact_info["contact_links"]],
    description="Select a resource:",
    disabled=False
)

# Create an output widget
output = widgets.Output()

# Define a function to handle dropdown changes
def on_change(change):
    with output:
        output.clear_output()  # Clear previous output
        selected_name = change["new"]
        for link in contact_info["contact_links"]:
            if link["name"] == selected_name:
                print(f"Selected: {link['name']}")
                print(f"URL: {link['url']}")
                if 'about' in link:
                    print(f"About: {link['about']}")
                break

# Observe the dropdown for changes
dropdown.observe(on_change, names="value")

# Display the dropdown and output widgets
display(dropdown, output)

