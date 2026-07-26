"""Generated from Smithy shape ``com.amazonaws.kms#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.tag_key_type
    import capo_kms.types.tag_value_type


class Tag(TypedDict, closed=True):
    tag_key: "capo_kms.types.tag_key_type.TagKeyType"
    """<p>The key of the tag.</p>"""
    tag_value: "capo_kms.types.tag_value_type.TagValueType"
    """<p>The value of the tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    out["TagValue"] = value["tag_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("Tag.tag_key required")
    if "TagValue" in data:
        out["tag_value"] = data["TagValue"]
    else:
        raise DeserializationError("Tag.tag_value required")
    return out
