---
name: Documentation
about: Update or add documentation
title: "[DOCS]: "
labels: documentation, needs-triage
---
Thanks for taking the time to fill out this out! :bow:
By submitting this issue, you agree to follow our [Code of Conduct](https://github.com/github/gh-copilot/blob/main/CODE_OF_CONDUCT.md).

### Describe the need
_What do you wish was different about our docs?_

### Version
_Do these docs apply to a specific version?_
_For example: `gh-copilot v0.5.2-beta`_

### Relevant terminal output
_Please copy and paste any relevant terminal output._
_Please check your output before submission to ensure sensitive information is redacted._
# prompt: name	about	title	labels
# Documentation
# Update or add documentation
# [DOCS]:
# documentation, needs-triage

import ipywidgets as widgets
from IPython.display import display

# This Python code represents the provided YAML structure as a Python dictionary.
# It's not directly executable in the context of creating a slider,
# but shows how to represent the data in Python.


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
            "about": "For more information on use cases, enabling, and limitations"
        },
        {
            "name": "Contact GitHub Support",
            "url": "https://support.github.com/request",
            "about": "Contact Support"
        }
    ]
}


# Example of accessing the data
# print(contact_info["blank_issues_enabled"])

# for link in contact_info["contact_links"]:
#     print(link["name"], link["url"])


# This code creates a slider in a Jupyter Notebook environment.
# The provided YAML data is not used in the slider creation.



# Create a slider widget
slider = widgets.IntSlider(
    value=5,  # Initial value of the slider
    min=0,    # Minimum value of the slider
    max=10,   # Maximum value of the slider
    step=1,   # Step size of the slider
    description='Slider:', # Description displayed next to the slider
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

# Display the slider
display(slider)

# You can access the slider's value using slider.value
# For example, to print the current value of the slider:
# print(slider.value)

# Added code to demonstrate using the contact information
print("\nContact Information:")
for link in contact_info["contact_links"]:
    print(f"- {link['name']}: {link['url']} ({link['about']})")
