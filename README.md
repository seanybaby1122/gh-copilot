# prompt: GitHub Copilot in the CLI is an extension for GitHub CLI which provides a chat-like interface in the terminal that allows you to ask questions about the command line. You can ask Copilot in the CLI to suggest a command for your use case with gh copilot suggest, or to explain a command you're curious about with gh copilot explain.
# For use cases, enabling, and limitations, see "GitHub Copilot in the CLI".
# For what data is collected, used, and shared, see "Privacy Policies".
# For help troubleshooting connectivity, see "Troubleshooting network errors for GitHub Copilot".
# Quickstart
# Note
# To use and install GitHub Copilot in the CLI, you must have an active GitHub Copilot subscription, have GitHub CLI installed, and authenticate using the GitHub CLI OAuth app.
# Classic and fine-grained PATs are currently unsupported and might require clearing the GITHUB_TOKEN and GH_TOKEN environment variables.
# Important
# GitHub Copilot in the CLI does not currently have plans to support 32-bit Android distributions.
# For more information, see https://github.com/github/gh-copilot/issues/122.
# Authenticate with GitHub CLI OAuth app
# gh auth login --web
# Install / upgrade extension
# gh extension install github/gh-copilot --force
# Suggest a command
# gh copilot suggest "Install and configure git lfs"
# Explain a command
# gh copilot explain 'git lfs migrate import --everything --include="*.gz,*.png,*.jar"'
# Usage
# $ gh copilot --help
# Your AI command line copilot.
# Usage:
#   copilot [command]
# Examples:
# $ gh copilot suggest "Install git"
# $ gh copilot explain "traceroute github.com"
# Available Commands:
#   alias       Generate shell-specific aliases for convenience
#   config      Configure options
#   explain     Explain a command
#   suggest     Suggest a command
# Flags:
#   -h, --help              help for copilot
#       --hostname string   The GitHub host to use for authentication
#   -v, --version           version for copilot
# Use "copilot [command] --help" for more information about a command.
# Multi-acco

# Install GitHub CLI if not already installed
!curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
!echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
!sudo apt update
!sudo apt install gh

# Authenticate with GitHub CLI (using web-based authentication)
!gh auth login --web

# Install the GitHub Copilot CLI extension
!gh extension install github/gh-copilot --force

# Example usage: Suggest a command to install Git LFS
!gh copilot suggest "Install and configure git lfs"

# Example usage: Explain a command
!gh copilot explain 'git lfs migrate import --everything --include="*.gz,*.png,*.jar"'


