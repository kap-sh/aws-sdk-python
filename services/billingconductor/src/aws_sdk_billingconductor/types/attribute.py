"""Generated from Smithy shape ``com.amazonaws.billingconductor#Attribute``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Attribute(TypedDict):
    key: NotRequired["str"]
    """<p>The key in a key-value pair that describes the margin summary.</p>"""
    value: NotRequired["str"]
    """<p>The value in a key-value pair that describes the margin summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attribute) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
