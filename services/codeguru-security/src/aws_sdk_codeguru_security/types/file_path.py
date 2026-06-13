"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#FilePath``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.code_snippet


class FilePath(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the file.</p>"""
    path: NotRequired["str"]
    """<p>The path to the resource with the security vulnerability.</p>"""
    start_line: NotRequired["int"]
    """<p>The first line number of the code snippet where the security vulnerability appears in your code.</p>"""
    end_line: NotRequired["int"]
    """<p>The last line number of the code snippet where the security vulnerability appears in your code.</p>"""
    code_snippet: NotRequired[
        "aws_sdk_codeguru_security.types.code_snippet.CodeSnippet"
    ]
    """<p>A list of <code>CodeLine</code> objects that describe where the security vulnerability appears in your code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilePath) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "path" in value:
        out["path"] = value["path"]
    if "start_line" in value:
        out["startLine"] = value["start_line"]
    if "end_line" in value:
        out["endLine"] = value["end_line"]
    if "code_snippet" in value:
        import aws_sdk_codeguru_security.types.code_snippet

        out["codeSnippet"] = (
            aws_sdk_codeguru_security.types.code_snippet.serialize_json(
                value["code_snippet"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilePath:
    out: FilePath = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "path" in data:
        out["path"] = data["path"]
    if "startLine" in data:
        out["start_line"] = data["startLine"]
    if "endLine" in data:
        out["end_line"] = data["endLine"]
    if "codeSnippet" in data:
        import aws_sdk_codeguru_security.types.code_snippet

        out["code_snippet"] = (
            aws_sdk_codeguru_security.types.code_snippet.deserialize_json(
                data["codeSnippet"]
            )
        )
    return out
