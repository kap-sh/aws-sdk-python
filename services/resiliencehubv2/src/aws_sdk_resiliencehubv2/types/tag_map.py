"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.tag_key
    import aws_sdk_resiliencehubv2.types.tag_value

TagMap: TypeAlias = dict[
    "aws_sdk_resiliencehubv2.types.tag_key.TagKey",
    "aws_sdk_resiliencehubv2.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TagMap:
    out: TagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
