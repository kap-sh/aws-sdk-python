"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.tag_key
    import aws_sdk_iotthingsgraph.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_iotthingsgraph.types.tag_key.TagKey"
    """<p>The required name of the tag. The string value can be from 1 to 128 Unicode characters in length.</p>"""
    value: "aws_sdk_iotthingsgraph.types.tag_value.TagValue"
    """<p>The optional value of the tag. The string value can be from 1 to 256 Unicode characters in length.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Tag.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Tag.value required")
    return out
