import ast
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]


def test_notebooks_are_valid_json_with_language_metadata():
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    assert notebooks
    for path in notebooks:
        document = json.loads(path.read_text(encoding="utf-8"))
        assert document["nbformat"] == 4
        for cell in document["cells"]:
            assert cell.get("metadata", {}).get("language") in {"markdown", "python"}
            if cell["cell_type"] == "code":
                ast.parse("".join(cell.get("source", [])), filename=str(path))


def test_expected_repository_directories_exist():
    for name in ("data", "docs", "notebooks", "results", "src", "tests"):
        assert (ROOT / name).is_dir()
