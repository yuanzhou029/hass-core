# GitHub Releases Publishing Guide

## Overview

This document explains how to publish the complete Home Assistant package to GitHub Releases using the enhanced workflow.

## Updated Workflow

The `.github/workflows/wheels.yml` workflow has been enhanced with a new job: `publish-complete-package`

This job only publishes the complete installation package (`homeassistant-complete-package.zip`) to GitHub Releases.

## How to Publish

### Prerequisites
- Ensure the main workflow (building wheels) has completed successfully
- Must be repository owner (yuanzhou029) with proper permissions
- Only triggers when a GitHub Release is published

### Steps

1. **Run the build workflow first**:
   - Go to the "Actions" tab in your repository
   - Select "Build Core Wheels with Custom Wheels Tool" workflow
   - Click "Run workflow" button
   - Make sure the "build-complete-package" job completes successfully

2. **Create a GitHub Release**:
   - Go to the "Releases" tab in your repository
   - Click "Draft a new release" or "Create a new release"
   - The release will trigger the `publish-complete-package` job automatically

3. **Automatic release publishing**:
   - The `publish-complete-package` job will attach the `homeassistant-complete-package.zip` to the release
   - This zip contains the complete installation package with precompiled dependencies

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