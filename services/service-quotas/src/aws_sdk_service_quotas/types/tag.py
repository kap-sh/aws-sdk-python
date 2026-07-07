"""Generated from Smithy shape ``com.amazonaws.servicequotas#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.tag_key
    import aws_sdk_service_quotas.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_service_quotas.types.tag_key.TagKey"
    """<p>A string that contains a tag key. The string length should be between 1 and 128 characters. Valid characters include a-z, A-Z, 0-9, space, and the special characters _ - . : / = + @.</p>"""
    value: "aws_sdk_service_quotas.types.tag_value.TagValue"
    """<p>A string that contains an optional tag value. The string length should be between 0 and 256 characters. Valid characters include a-z, A-Z, 0-9, space, and the special characters _ - . : / = + @.</p>"""


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
