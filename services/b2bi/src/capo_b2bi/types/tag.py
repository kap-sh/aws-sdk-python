"""Generated from Smithy shape ``com.amazonaws.b2bi#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.tag_key
    import capo_b2bi.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_b2bi.types.tag_key.TagKey"
    """<p>Specifies the name assigned to the tag that you create.</p>"""
    value: "capo_b2bi.types.tag_value.TagValue"
    """<p>Contains one or more values that you assigned to the key name that you create.</p>"""


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
