"""Generated from Smithy shape ``com.amazonaws.voiceid#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import capo_voice_id.types.tag_key
    import capo_voice_id.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_voice_id.types.tag_key.TagKey"
    """<p>The first part of a key:value pair that forms a tag associated with a given resource. For example, in the tag 'Department':'Sales', the key is 'Department'. </p>"""
    value: "capo_voice_id.types.tag_value.TagValue"
    """<p>The second part of a key:value pair that forms a tag associated with a given resource. For example, in the tag 'Department':'Sales', the value is 'Sales'. </p>"""


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
