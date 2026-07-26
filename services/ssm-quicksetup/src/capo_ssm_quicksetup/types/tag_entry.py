"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#TagEntry``."""

from typing_extensions import NotRequired, TypedDict


class TagEntry(TypedDict, closed=True):
    key: NotRequired["str"]
    """<p>The key for the tag.</p>"""
    value: NotRequired["str"]
    """<p>The value for the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagEntry) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagEntry:
    out: TagEntry = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
