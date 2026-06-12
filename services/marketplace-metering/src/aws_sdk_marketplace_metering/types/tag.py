"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_metering.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.tag_key
    import aws_sdk_marketplace_metering.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_marketplace_metering.types.tag_key.TagKey"
    """<p>One part of a key-value pair that makes up a <code>tag</code>. A <code>key</code> is a label that acts like a category for the specific tag values.</p>"""
    value: "aws_sdk_marketplace_metering.types.tag_value.TagValue"
    """<p>One part of a key-value pair that makes up a <code>tag</code>. A <code>value</code> acts as a descriptor within a tag category (key). The value can be empty or null.</p>"""


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
