"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeLocation``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_securityagent.errors import DeserializationError


class CodeLocation(TypedDict):
    file_path: "str"
    """<p>The absolute path to the file containing the code location.</p>"""
    line_start: NotRequired["int"]
    """<p>The starting line number of the code location.</p>"""
    line_end: NotRequired["int"]
    """<p>The ending line number of the code location.</p>"""
    label: NotRequired["str"]
    """<p>The role of this location in the vulnerability, such as source or sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeLocation) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    if "line_start" in value:
        out["lineStart"] = value["line_start"]
    if "line_end" in value:
        out["lineEnd"] = value["line_end"]
    if "label" in value:
        out["label"] = value["label"]
    return out


def deserialize_json(data: dict) -> CodeLocation:
    out: CodeLocation = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("CodeLocation.file_path required")
    if "lineStart" in data:
        out["line_start"] = data["lineStart"]
    if "lineEnd" in data:
        out["line_end"] = data["lineEnd"]
    if "label" in data:
        out["label"] = data["label"]
    return out
