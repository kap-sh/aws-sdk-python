"""Generated from Smithy shape ``com.amazonaws.forecast#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.tag_key
    import aws_sdk_forecast.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_forecast.types.tag_key.TagKey"
    """<p>One part of a key-value pair that makes up a tag. A <code>key</code> is a general label that acts like a category for more specific tag values.</p>"""
    value: "aws_sdk_forecast.types.tag_value.TagValue"
    """<p>The optional part of a key-value pair that makes up a tag. A <code>value</code> acts as a descriptor within a tag category (key).</p>"""


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
