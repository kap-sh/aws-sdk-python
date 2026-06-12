"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Position``."""

from typing import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError


class Position(TypedDict):
    line: "int"
    """<p>The line of the position, starting from 1.</p>"""
    column: "int"
    """<p>The column of the position, starting from 0.</p>"""
    offset: "int"
    """<p>The offset within the policy that corresponds to the position, starting from 0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Position) -> dict:
    out: dict = {}
    out["line"] = value["line"]
    out["column"] = value["column"]
    out["offset"] = value["offset"]
    return out


def deserialize_json(data: dict) -> Position:
    out: Position = {}  # type: ignore[typeddict-item]
    if "line" in data:
        out["line"] = data["line"]
    else:
        raise DeserializationError("Position.line required")
    if "column" in data:
        out["column"] = data["column"]
    else:
        raise DeserializationError("Position.column required")
    if "offset" in data:
        out["offset"] = data["offset"]
    else:
        raise DeserializationError("Position.offset required")
    return out
