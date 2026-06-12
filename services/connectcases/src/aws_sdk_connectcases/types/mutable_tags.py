"""Generated from Smithy shape ``com.amazonaws.connectcases#MutableTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.mutable_tag_key
    import aws_sdk_connectcases.types.tag_value_string

MutableTags: TypeAlias = dict[
    "aws_sdk_connectcases.types.mutable_tag_key.MutableTagKey",
    "aws_sdk_connectcases.types.tag_value_string.TagValueString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MutableTags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MutableTags:
    out: MutableTags = {}
    for key, value in data.items():
        out[key] = value
    return out
