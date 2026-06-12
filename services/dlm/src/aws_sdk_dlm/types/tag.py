"""Generated from Smithy shape ``com.amazonaws.dlm#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.string


class Tag(TypedDict):
    key: NotRequired["aws_sdk_dlm.types.string.String"]
    """<p>The tag key.</p>"""
    value: NotRequired["aws_sdk_dlm.types.string.String"]
    """<p>The tag value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
