"""Generated from Smithy shape ``com.amazonaws.mpa#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.tag_key
    import aws_sdk_mpa.types.tag_value

Tags: TypeAlias = dict[
    "aws_sdk_mpa.types.tag_key.TagKey", "aws_sdk_mpa.types.tag_value.TagValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
