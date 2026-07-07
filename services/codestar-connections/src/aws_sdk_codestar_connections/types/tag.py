"""Generated from Smithy shape ``com.amazonaws.codestarconnections#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.tag_key
    import aws_sdk_codestar_connections.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_codestar_connections.types.tag_key.TagKey"
    """<p>The tag's key.</p>"""
    value: "aws_sdk_codestar_connections.types.tag_value.TagValue"
    """<p>The tag's value.</p>"""


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
