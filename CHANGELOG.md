# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

## [0.0.2] - 2026-09-24

### Added

- `pygcgb` console script entry point.
- `py.typed` marker, so the installed package ships its type information.
- Hatchling wheel target that packages `src/pygcgb`.

### Changed

- Renamed the distribution from `template` to `py-gcgbarbosa`.
- Moved the entrypoint from `src/app.py` to `src/pygcgb/main.py`.
- Replaced the pre-commit hook manager with lefthook.
- Added explicit project metadata (license, authors, classifiers, urls) and a
  ruff lint ruleset (`I`, `UP`, `B`, `SIM`, `RUF`).
- Coverage configuration now targets the `pygcgb` package instead of `src`.

### Removed

- Unused `loguru` runtime dependency.

## [0.0.1] - 2025-04-09

### Added

- First release of the project
