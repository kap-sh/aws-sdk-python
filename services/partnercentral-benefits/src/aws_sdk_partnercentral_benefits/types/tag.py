"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_benefits.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.tag_key
    import aws_sdk_partnercentral_benefits.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_partnercentral_benefits.types.tag_key.TagKey"
    """<p>The tag key, which acts as a category or label for the tag.</p>"""
    value: "aws_sdk_partnercentral_benefits.types.tag_value.TagValue"
    """<p>The tag value, which provides additional information or context for the tag key.</p>"""


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
