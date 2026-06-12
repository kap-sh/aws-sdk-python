"""Generated from Smithy shape ``com.amazonaws.macie2#KeyValuePair``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class KeyValuePair(TypedDict):
    key: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>One part of a key-value pair that comprises a tag. A tag key is a general label that acts as a category for more specific tag values.</p>"""
    value: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>One part of a key-value pair that comprises a tag. A tag value acts as a descriptor for a tag key. A tag value can be an empty string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyValuePair) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> KeyValuePair:
    out: KeyValuePair = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
