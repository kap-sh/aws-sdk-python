"""Generated from Smithy shape ``com.amazonaws.kendraranking#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.tag_key
    import aws_sdk_kendra_ranking.types.tag_value


class Tag(TypedDict, closed=True):
    key: "aws_sdk_kendra_ranking.types.tag_key.TagKey"
    """<p>The key for the tag. Keys are not case sensitive and must be unique.</p>"""
    value: "aws_sdk_kendra_ranking.types.tag_value.TagValue"
    """<p>The value associated with the tag. The value can be an empty string but it can't be null.</p>"""


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
