# ----------------------------------------------------------------------
# WORKFLOW NAME - Just for display in GitHub Actions tab
# Think of it like a title for your automation recipe
# ----------------------------------------------------------------------
name: python-calulator-test  # Shows up as "python-calulator-test" in GitHub UI

# ----------------------------------------------------------------------
# TRIGGERS - WHEN should this workflow start?
# Like telling GitHub: "Hey, wake up and run this when..."
# ----------------------------------------------------------------------
on:  # Start of trigger conditions
    push:  # Event type: Someone pushes/upload code
        branches: [ main ]  # Only care about pushes to 'main' branch
        # So if someone pushes to 'feature' branch, this WON'T run
    
    pull_request:  # Event type: Someone creates/updates a PR
        branches: [ main ]  # Only for PRs that want to merge into 'main'
        # This runs when PR is opened, updated, or reopened

# ----------------------------------------------------------------------
# JOBS - WHAT tasks need to be done?
# Each job runs in its own fresh environment (like separate computers)
# ----------------------------------------------------------------------
jobs:  # Container for all jobs
    tests:  # Job ID - you can name this anything (build, check, deploy, etc.)
        # ------------------------------------------------------------------
        # RUNNER - WHERE will this job execute?
        # GitHub creates a fresh virtual machine with this OS
        # ------------------------------------------------------------------
        runs-on: ubuntu:latest  # Using Ubuntu Linux (latest version)
        # Other options: windows-latest, macos-latest, ubuntu-20.04

        # ------------------------------------------------------------------
        # STEPS - The actual commands (like a to-do list)
        # Each step runs in order, one after another
        # If any step fails (non-zero exit code), the whole job fails
        # ------------------------------------------------------------------
        steps:
            # ------------------------------------------------------------------
            # STEP 1: Download your code
            # This is ALWAYS needed as first step because the runner starts empty
            # ------------------------------------------------------------------
            - name: Get Code from github  # Human-readable description
              uses: actions/checkout@v3   # Pre-made action that downloads repo
              # What this does behind scenes: 
              # - Connects to GitHub API
              # - Downloads your entire repository
              # - Puts it in the runner's file system

            # ------------------------------------------------------------------
            # STEP 2: Install Python
            # Without this, the runner has no Python installed!
            # ------------------------------------------------------------------
            - name: Setup Python
              uses: actions/setup-python@v4  # Official Python installer action
              with:  # Parameters/options for this action
                python-version: "3.10"  # Specifically install Python 3.10
                # This action also adds 'python' command to PATH automatically

            # ------------------------------------------------------------------
            # STEP 3: Install project dependencies
            # Like running 'npm install' but for Python
            # ------------------------------------------------------------------
            - name: Install dependencies
              run: |  # The | means "multiple lines of commands coming up"
                # First: Upgrade pip (Python's package installer) to latest version
                # --upgrade means "get latest version"
                python -m pip install --upgrade pip
                
                # Second: Check if requirements.txt exists
                # [ -f requirements.txt ] is bash for "check if file exists"
                # If it exists, install all packages listed in it
                # -r means "read from file"
                if [ -f requirements.txt ]; then pip install requirements.txt; fi
                # The ; fi closes the if statement in bash

            # ------------------------------------------------------------------
            # STEP 4: Actually run the tests
            # This is the MAIN purpose of this workflow!
            # ------------------------------------------------------------------
            - name: Run tests
              run: python test_calulator.py  # Execute test file
              # If any test fails (assert fails), Python exits with code 1
              # Exit code 1 = failure, which stops the workflow here

            # ------------------------------------------------------------------
            # STEP 5: Celebrate success (optional)
            # Only runs if ALL previous steps succeeded
            # ------------------------------------------------------------------
            - name: validation
              if: success()  # Condition: only if previous steps all passed
              run: "All tests pass successfully!!"  # Happy message
              # success() is a built-in function that returns true if no errors yet

# ----------------------------------------------------------------------
# FLOW VISUALIZATION:
# 
# push to main ──┐
#                ├─► Trigger workflow ──► Create Ubuntu VM ──►
# PR to main ────┘
# 
# Step 1: Checkout code (get repo)
#         ↓
# Step 2: Setup Python 3.10
#         ↓
# Step 3: Install dependencies (if any)
#         ↓
# Step 4: Run tests
#         ↓
#      [if all pass] ──► Step 5: Celebration message
#      [if any fail] ──► Stop here, mark as failed ❌
# ----------------------------------------------------------------------

# 💡 PRO TIPS:
# 1. You can have multiple jobs that run in parallel
# 2. Each step runs in the same terminal session (so env vars persist)
# 3. The runner VM is destroyed after job completes (cost saving!)
# 4. All output/logs are saved and viewable in GitHub UI

# 🎯 GitHub Actions Quick Reference Card

A handy cheat sheet for the most common GitHub Actions YAML syntax elements.

## Core Structure Elements

| Syntax       | Meaning                              | Example                                      |
|--------------|--------------------------------------|----------------------------------------------|
| `name`       | Workflow display name                | `name: CI Pipeline`                          |
| `on`         | Trigger events                       | `on: [push, pull_request]`                   |
| `jobs`       | Container for all tasks/jobs         | `jobs: { build: { ... } }`                   |
| `runs-on`    | Operating system / runner to use     | `runs-on: ubuntu-latest`                     |
| `steps`      | List of commands / actions to run    | `steps: [ - name: Checkout code ]`           |
| `uses`       | Use a pre-built action from marketplace | `uses: actions/checkout@v4`                 |
| `run`        | Run a shell command                  | `run: python -m pytest`                      |
| `with`       | Pass parameters to an action         | `with: { token: ${{ secrets.GITHUB_TOKEN }} }` |
| `if`         | Conditional execution of step/job    | `if: success()` or `if: github.ref == 'refs/heads/main'` |

## Popular Trigger Examples (`on:`)

```yaml
# Basic triggers
on: [push, pull_request]

# More specific
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 5 * * 1'   # Every Monday at 5:00 UTC
  workflow_dispatch:       # Manual trigger button

## Useful Conditionals (if:)

# Common patterns
if: github.event_name == 'push'
if: contains(github.event.head_commit.message, '[skip ci]')
if: success()               # Previous step succeeded
if: failure()               # Previous step failed
if: always()                # Run even if previous failed
if: cancelled()             # Workflow was cancelled

