"""Generated from Smithy shape ``com.amazonaws.dynamodb#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.tag_key_string
    import aws_sdk_dynamodb.types.tag_value_string


class Tag(TypedDict, closed=True):
    key: "aws_sdk_dynamodb.types.tag_key_string.TagKeyString"
    """<p>The key of the tag. Tag keys are case sensitive. Each DynamoDB table can only have up to one tag with the same key. If you try to add an existing tag (same key), the existing tag value will be updated to the new value.</p>"""
    value: "aws_sdk_dynamodb.types.tag_value_string.TagValueString"
    """<p>The value of the tag. Tag values are case-sensitive and can be null.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
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
