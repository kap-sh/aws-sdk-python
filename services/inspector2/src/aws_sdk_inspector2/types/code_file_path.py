"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeFilePath``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.non_empty_string


class CodeFilePath(TypedDict, closed=True):
    file_name: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The name of the file the code vulnerability was found in.</p>"""
    file_path: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The file path to the code that a vulnerability was found in.</p>"""
    start_line: "int"
    """<p>The line number of the first line of code that a vulnerability was found in.</p>"""
    end_line: "int"
    """<p>The line number of the last line of code that a vulnerability was found in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeFilePath) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    out["filePath"] = value["file_path"]
    out["startLine"] = value["start_line"]
    out["endLine"] = value["end_line"]
    return out


def deserialize_json(data: dict) -> CodeFilePath:
    out: CodeFilePath = {}  # type: ignore[typeddict-item]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("CodeFilePath.file_name required")
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("CodeFilePath.file_path required")
    if "startLine" in data:
        out["start_line"] = data["startLine"]
    else:
        raise DeserializationError("CodeFilePath.start_line required")
    if "endLine" in data:
        out["end_line"] = data["endLine"]
    else:
        raise DeserializationError("CodeFilePath.end_line required")
    return out
