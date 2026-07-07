"""Generated from Smithy shape ``com.amazonaws.workspacesweb#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.tag_key
    import aws_sdk_workspaces_web.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_workspaces_web.types.tag_key.TagKey"
    """<p>The key of the tag.</p>"""
    value: "aws_sdk_workspaces_web.types.tag_value.TagValue"
    """<p>The value of the tag</p>"""


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
