"""Generated from Smithy shape ``com.amazonaws.macie2#TagValuePair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class TagValuePair(TypedDict, closed=True):
    key: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The value for the tag key to use in the condition.</p>"""
    value: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The tag value, associated with the specified tag key (key), to use in the condition. To specify only a tag key for a condition, specify the tag key for the key property and set this value to an empty string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagValuePair) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagValuePair:
    out: TagValuePair = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
