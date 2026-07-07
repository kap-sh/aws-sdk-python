"""Generated from Smithy shape ``com.amazonaws.socialmessaging#Tag``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError


class Tag(TypedDict, closed=True):
    key: "str"
    """<p>The tag key.</p>"""
    value: NotRequired["str"]
    """<p>The tag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if "value" in data:
        out["value"] = data["value"]
    return out
