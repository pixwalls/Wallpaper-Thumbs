name: Auto Shuffle JSON

on:
  schedule:
    - cron: '*/1 * * * *'  # Every 1 minute
  workflow_dispatch:       # Manual trigger

jobs:
  shuffle:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Run Shuffle Script
        run: python shuffle_json.py

      - name: Commit and Push Changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add "pixwalls - fixed.json"
          git commit -m "Auto-shuffled JSON" || echo "No changes to commit"
          git push
