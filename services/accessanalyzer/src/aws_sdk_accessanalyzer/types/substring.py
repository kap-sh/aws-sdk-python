"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Substring``."""

from typing import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError


class Substring(TypedDict):
    start: "int"
    """<p>The start index of the substring, starting from 0.</p>"""
    length: "int"
    """<p>The length of the substring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Substring) -> dict:
    out: dict = {}
    out["start"] = value["start"]
    out["length"] = value["length"]
    return out


def deserialize_json(data: dict) -> Substring:
    out: Substring = {}  # type: ignore[typeddict-item]
    if "start" in data:
        out["start"] = data["start"]
    else:
        raise DeserializationError("Substring.start required")
    if "length" in data:
        out["length"] = data["length"]
    else:
        raise DeserializationError("Substring.length required")
    return out
