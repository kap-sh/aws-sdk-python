"""Generated from Smithy shape ``com.amazonaws.personalize#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.tag_key
    import aws_sdk_personalize.types.tag_value


class Tag(TypedDict, closed=True):
    tag_key: "aws_sdk_personalize.types.tag_key.TagKey"
    """<p>One part of a key-value pair that makes up a tag. A key is a general label that acts like a category for more specific tag values.</p>"""
    tag_value: "aws_sdk_personalize.types.tag_value.TagValue"
    """<p>The optional part of a key-value pair that makes up a tag. A value acts as a descriptor within a tag category (key).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["tagKey"] = value["tag_key"]
    out["tagValue"] = value["tag_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "tagKey" in data:
        out["tag_key"] = data["tagKey"]
    else:
        raise DeserializationError("Tag.tag_key required")
    if "tagValue" in data:
        out["tag_value"] = data["tagValue"]
    else:
        raise DeserializationError("Tag.tag_value required")
    return out
