"""Generated from Smithy shape ``com.amazonaws.rum#DimensionKeysMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rum.types.dimension_key
    import aws_sdk_rum.types.dimension_name

DimensionKeysMap: TypeAlias = dict[
    "aws_sdk_rum.types.dimension_key.DimensionKey",
    "aws_sdk_rum.types.dimension_name.DimensionName",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DimensionKeysMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DimensionKeysMap:
    out: DimensionKeysMap = {}
    for key, value in data.items():
        out[key] = value
    return out
