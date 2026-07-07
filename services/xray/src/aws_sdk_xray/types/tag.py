"""Generated from Smithy shape ``com.amazonaws.xray#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.tag_key
    import aws_sdk_xray.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_xray.types.tag_key.TagKey"
    """<p>A tag key, such as <code>Stage</code> or <code>Name</code>. A tag key cannot be empty. The key can be a maximum of 128 characters, and can contain only Unicode letters, numbers, or separators, or the following special characters: <code>+ - = . _ : /</code> </p>"""
    value: "aws_sdk_xray.types.tag_value.TagValue"
    """<p>An optional tag value, such as <code>Production</code> or <code>test-only</code>. The value can be a maximum of 255 characters, and contain only Unicode letters, numbers, or separators, or the following special characters: <code>+ - = . _ : /</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("Tag.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
