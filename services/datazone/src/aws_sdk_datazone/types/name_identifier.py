"""Generated from Smithy shape ``com.amazonaws.datazone#NameIdentifier``."""

from typing import TypedDict

from typing_extensions import NotRequired


class NameIdentifier(TypedDict):
    name: NotRequired["str"]
    """<p>The name in the name identifier.</p>"""
    namespace: NotRequired["str"]
    """<p>The namespace in the name identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NameIdentifier) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> NameIdentifier:
    out: NameIdentifier = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    return out
