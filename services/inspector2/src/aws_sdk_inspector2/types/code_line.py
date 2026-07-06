"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeLine``."""

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError


class CodeLine(TypedDict, closed=True):
    content: "str"
    """<p>The content of a line of code</p>"""
    line_number: "int"
    """<p>The line number that a section of code is located at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeLine) -> dict:
    out: dict = {}
    out["content"] = value["content"]
    out["lineNumber"] = value["line_number"]
    return out


def deserialize_json(data: dict) -> CodeLine:
    out: CodeLine = {}  # type: ignore[typeddict-item]
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("CodeLine.content required")
    if "lineNumber" in data:
        out["line_number"] = data["lineNumber"]
    else:
        raise DeserializationError("CodeLine.line_number required")
    return out
