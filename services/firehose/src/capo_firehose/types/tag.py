"""Generated from Smithy shape ``com.amazonaws.firehose#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.tag_key
    import capo_firehose.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_firehose.types.tag_key.TagKey"
    """<p>A unique identifier for the tag. Maximum length: 128 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @</p>"""
    value: NotRequired["capo_firehose.types.tag_value.TagValue"]
    """<p>An optional string, which you can use to describe or define the tag. Maximum length: 256 characters. Valid characters: Unicode letters, digits, white space, _ . / = + - % @</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
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
    return out
