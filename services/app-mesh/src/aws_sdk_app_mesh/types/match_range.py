"""Generated from Smithy shape ``com.amazonaws.appmesh#MatchRange``."""

from typing_extensions import TypedDict

from aws_sdk_app_mesh.errors import DeserializationError


class MatchRange(TypedDict, closed=True):
    start: "int"
    """<p>The start of the range.</p>"""
    end: "int"
    """<p>The end of the range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatchRange) -> dict:
    out: dict = {}
    out["start"] = value["start"]
    out["end"] = value["end"]
    return out


def deserialize_json(data: dict) -> MatchRange:
    out: MatchRange = {}  # type: ignore[typeddict-item]
    if "start" in data:
        out["start"] = data["start"]
    else:
        raise DeserializationError("MatchRange.start required")
    if "end" in data:
        out["end"] = data["end"]
    else:
        raise DeserializationError("MatchRange.end required")
    return out
