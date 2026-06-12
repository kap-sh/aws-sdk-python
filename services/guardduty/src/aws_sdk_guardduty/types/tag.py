"""Generated from Smithy shape ``com.amazonaws.guardduty#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class Tag(TypedDict):
    key: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Describes the key associated with the tag.</p>"""
    value: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Describes the value associated with the tag key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out
