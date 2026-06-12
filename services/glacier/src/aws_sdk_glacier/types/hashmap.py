"""Generated from Smithy shape ``com.amazonaws.glacier#hashmap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string

hashmap: TypeAlias = dict[
    "aws_sdk_glacier.types.string.string", "aws_sdk_glacier.types.string.string"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: hashmap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> hashmap:
    out: hashmap = {}
    for key, value in data.items():
        out[key] = value
    return out
