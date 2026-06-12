"""Generated from Smithy shape ``com.amazonaws.timestreamquery#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.tag_key
    import aws_sdk_timestream_query.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_timestream_query.types.tag_key.TagKey"
    """<p>The key of the tag. Tag keys are case sensitive. </p>"""
    value: "aws_sdk_timestream_query.types.tag_value.TagValue"
    """<p>The value of the tag. Tag values are case sensitive and can be null. </p>"""


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
