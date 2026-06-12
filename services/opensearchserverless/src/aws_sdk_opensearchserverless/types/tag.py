"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.tag_key
    import aws_sdk_opensearchserverless.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_opensearchserverless.types.tag_key.TagKey"
    """<p>The key to use in the tag.</p>"""
    value: "aws_sdk_opensearchserverless.types.tag_value.TagValue"
    """<p>The value of the tag.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
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
