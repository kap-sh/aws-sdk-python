"""Generated from Smithy shape ``com.amazonaws.cloud9#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.tag_key
    import aws_sdk_cloud9.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_cloud9.types.tag_key.TagKey"
    """<p>The <b>name</b> part of a tag.</p>"""
    value: "aws_sdk_cloud9.types.tag_value.TagValue"
    """<p>The <b>value</b> part of a tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
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
