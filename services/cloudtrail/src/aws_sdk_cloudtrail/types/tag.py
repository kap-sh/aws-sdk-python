"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.tag_key
    import aws_sdk_cloudtrail.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_cloudtrail.types.tag_key.TagKey"
    """<p>The key in a key-value pair. The key must be must be no longer than 128 Unicode characters. The key must be unique for the resource to which it applies.</p>"""
    value: NotRequired["aws_sdk_cloudtrail.types.tag_value.TagValue"]
    """<p>The value in a key-value pair of a tag. The value must be no longer than 256 Unicode characters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
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
    return out
