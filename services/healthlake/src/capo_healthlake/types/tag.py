"""Generated from Smithy shape ``com.amazonaws.healthlake#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.tag_key
    import capo_healthlake.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_healthlake.types.tag_key.TagKey"
    """<p>The key portion of a tag. Tag keys are case sensitive. </p>"""
    value: "capo_healthlake.types.tag_value.TagValue"
    """<p> The value portion of a tag. Tag values are case-sensitive.</p>"""


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
