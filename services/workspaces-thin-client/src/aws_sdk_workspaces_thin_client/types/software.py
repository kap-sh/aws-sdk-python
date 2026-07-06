"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#Software``."""

from typing_extensions import NotRequired, TypedDict


class Software(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the software component.</p>"""
    version: NotRequired["str"]
    """<p>The version of the software component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Software) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> Software:
    out: Software = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    return out
