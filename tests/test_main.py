from template.app import main


def test_main_output_and_return(capsys):
    result = main()
    captured = capsys.readouterr()

    assert "Hello from template!" in captured.out

    assert result == 2
