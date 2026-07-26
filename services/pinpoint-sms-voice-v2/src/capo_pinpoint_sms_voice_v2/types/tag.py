"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.tag_key
    import capo_pinpoint_sms_voice_v2.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_pinpoint_sms_voice_v2.types.tag_key.TagKey"
    """<p>The key identifier, or name, of the tag.</p>"""
    value: "capo_pinpoint_sms_voice_v2.types.tag_value.TagValue"
    """<p>The string value associated with the key of the tag.</p>"""


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
