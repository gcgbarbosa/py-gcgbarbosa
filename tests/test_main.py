"""Tests for the CLI entrypoint."""

import runpy
import sys

from pygcgb.main import app


def test_app_output_and_return(capsys):
    """`app` greets on stdout and returns 1 + 1."""
    result = app()
    captured = capsys.readouterr()

    assert "Hello from template!" in captured.out
    assert result == 2


def test_main_block():
    """Running the module as a script executes the entrypoint."""
    module_name = "pygcgb.main"
    sys.modules.pop(module_name, None)

    runpy.run_module(module_name, run_name="__main__")
