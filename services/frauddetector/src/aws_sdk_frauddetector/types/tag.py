"""Generated from Smithy shape ``com.amazonaws.frauddetector#Tag``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.tag_key
    import aws_sdk_frauddetector.types.tag_value


class Tag(TypedDict):
    key: "aws_sdk_frauddetector.types.tag_key.tagKey"
    """<p>A tag key.</p>"""
    value: "aws_sdk_frauddetector.types.tag_value.tagValue"
    """<p>A value assigned to a tag key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Tag) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Tag:
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
