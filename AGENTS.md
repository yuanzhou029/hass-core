# Home Assistant Core Development Guide

This repository contains the core of Home Assistant, a Python 3 based home automation application.

## Build/Lint/Test Commands

### Building and Setup
- `python -m venv venv && source venv/bin/activate && pip install "$(grep '^uv' < requirements.txt)" && uv pip install -r requirements.txt` - Setup development environment
- `python -m script.gen_requirements_all ci` - Generate requirements files

### Linting
- `ruff check .` - Run ruff linter
- `ruff format .` - Format code with ruff
- `pylint homeassistant` - Run pylint on core
- `pylint tests` - Run pylint on tests
- `mypy homeassistant` - Run mypy type checking
- `codespell .` - Check for spelling errors
- `pre-commit run --all-files` - Run all pre-commit checks

### Testing
- `python -m pytest tests/<path_to_test>` - Run specific test file
- `python -m pytest tests/components/<integration_name>/` - Run tests for specific integration
- `python -m pytest tests/<path_to_test>::<test_function_name>` - Run specific test function
- `python -m pytest --cov=homeassistant tests/<path_to_test>` - Run tests with coverage
- `python -m pytest --lf` - Run last failed tests
- `python -m pytest --pdb` - Drop into debugger on test failure
- `python -m pytest -k <keyword>` - Run tests matching keyword
- `python -m pytest -m <marker>` - Run tests with specific marker

## Code Style Guidelines

### Imports
- Group imports in order: standard library, third-party, first-party
- Use absolute imports for internal modules
- Import only what you need (avoid `from module import *`)
- Sort imports alphabetically within groups

### Formatting
- Use Ruff formatter (based on Black style)
- 88 character line length limit
- Use single quotes for strings unless double quotes are needed
- Use f-strings for string formatting
- Follow PEP 8 guidelines

### Type Hints
- All public functions/methods must have type hints
- Use modern Python generics (e.g., `list[str]` instead of `List[str]`)
- Use `from __future__ import annotations` for forward references
- Use `typing_extensions` for newer typing features
- Follow strict typing guidelines in `.strict-typing` file

### Naming Conventions
- Use snake_case for functions, variables, and modules
- Use PascalCase for classes
- Use UPPER_CASE for constants
- Prefix private methods/attributes with underscore
- Use descriptive names that clearly express intent

### Error Handling
- Use specific exception types rather than generic Exception
- Catch specific exceptions rather than broad except clauses
- Include meaningful error messages
- Use context managers where appropriate
- Follow Python 3.14 syntax: `except TypeA, TypeB:` without parentheses is allowed

### Code Organization
- Keep functions small and focused on a single responsibility
- Follow the existing architectural patterns
- Place type imports behind TYPE_CHECKING guards when needed to avoid runtime overhead
- Document public APIs with docstrings in Google style

### Testing Practices
- Write unit tests for all new functionality
- Use pytest fixtures for test setup/teardown
- Name tests descriptively with `test_` prefix
- Test edge cases and error conditions
- Use mocking appropriately for external dependencies
- Follow AAA pattern (Arrange, Act, Assert)

### Integration Development
- Follow the integration quality scale guidelines
- Use Platinum/Gold level integrations as examples
- Include proper manifest.json with quality scale indicator
- Implement proper setup and teardown procedures
- Handle configuration validation appropriately

## Development Workflow

### Pre-commit Hooks
- Install with `pip install pre-commit && pre-commit install`
- Hooks run automatically on commit
- Includes ruff, codespell, mypy, pylint, and other checks

### Code Review Guidelines
- Do NOT amend, squash, or rebase commits after review has started
- Reviewers need to see what changed since their last review
- Address review comments with new commits rather than modifying existing ones

### Good Practices
- Reference Platinum or Gold level integrations for code quality examples
- Use the development commands in `.vscode/tasks.json`
- Keep up with dependency updates regularly
- Follow security best practices when handling user data
