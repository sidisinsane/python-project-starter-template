"""Demo example of how to test a copier template with pytest-copie."""

from typing import Any


def test_template_with_extra_answers(copie: Any) -> None:
    """Test the demo copier template with extra answers using pytest-copie."""
    result = copie.copy(
        extra_answers={
            "project_name": "Test",
            "project_description": "This is a test description.",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir / "README.md") as f:
        assert f.readline() == '<h1 align="center">\n'
