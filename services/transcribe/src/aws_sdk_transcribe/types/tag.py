"""Generated from Smithy shape ``com.amazonaws.transcribe#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.tag_key
    import aws_sdk_transcribe.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_transcribe.types.tag_key.TagKey"
    """<p>The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag <code>Department:Sales</code>, the key is 'Department'.</p>"""
    value: "aws_sdk_transcribe.types.tag_value.TagValue"
    """<p>The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag <code>Department:Sales</code>, the value is 'Sales'.</p> <p>Note that you can set the value of a tag to an empty string, but you can't set the value of a tag to null. Omitting the tag value is the same as using an empty string.</p>"""


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
