"""Generated from Smithy shape ``com.amazonaws.managedblockchain#InputTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.tag_key
    import aws_sdk_managedblockchain.types.tag_value

InputTagMap: TypeAlias = dict[
    "aws_sdk_managedblockchain.types.tag_key.TagKey",
    "aws_sdk_managedblockchain.types.tag_value.TagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: InputTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> InputTagMap:
    out: InputTagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
