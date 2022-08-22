terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
    token="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"
}

# Add a user to the organization
resource "github_membership" "membership_for_user_x" {
  # ...
}