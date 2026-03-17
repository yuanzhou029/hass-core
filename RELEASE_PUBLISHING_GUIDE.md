# GitHub Releases Publishing Guide

## Overview

This document explains how to publish built Home Assistant wheels to GitHub Releases using the enhanced workflow.

## Updated Workflow

The `.github/workflows/wheels.yml` workflow has been enhanced with a new job: `publish-to-github-releases`

This job:
1. Collects all built wheels from previous jobs
2. Creates a release with all wheel packages
3. Publishes to GitHub Releases with a summary

## How to Publish

### Prerequisites
- Ensure the main workflow (building wheels) has completed successfully
- Must be repository owner (yuanzhou029) with proper permissions

### Steps

1. **Run the workflow manually**:
   - Go to the "Actions" tab in your repository
   - Select "Build Core Wheels with Custom Wheels Tool" workflow
   - Click "Run workflow" button
   - Select "Run workflow" (it should run via `workflow_dispatch`)

2. **Wait for build completion**:
   - The workflow will execute the build jobs first:
     - init
     - core (build core wheels)
     - integrations (build integration wheels)
     - build-complete-package (create complete package)

3. **Automatic release**:
   - Once all building jobs complete successfully
   - The `publish-to-github-releases` job will trigger automatically
   - This job collects all artifacts and creates a GitHub Release

## Release Contents

Each release includes:
- All precompiled wheel packages (core and integrations)
- Complete Home Assistant package with dependencies
- Asset summary with file list and sizes
- Installation instructions

## Release Naming Convention

- Name: `Home Assistant Prebuilt Dependencies v{VERSION}`
- Tag: `v{VERSION}_deps`
- Where `{VERSION}` is extracted from the Home Assistant package name

## Permissions

The workflow includes necessary permissions:
```yaml
permissions:
  contents: write  # Required for creating releases
```

## Troubleshooting

- If the release job doesn't run, check that all prerequisite jobs completed successfully
- Ensure your repository has the required permissions for creating releases
- The release only happens on `workflow_dispatch` events, not scheduled runs