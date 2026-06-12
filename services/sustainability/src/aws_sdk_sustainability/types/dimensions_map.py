"""Generated from Smithy shape ``com.amazonaws.sustainability#DimensionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sustainability.types.dimension

DimensionsMap: TypeAlias = dict[
    "aws_sdk_sustainability.types.dimension.Dimension", "str"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DimensionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sustainability.types.dimension

        out[aws_sdk_sustainability.types.dimension.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> DimensionsMap:
    out: DimensionsMap = {}
    for key, value in data.items():
        import aws_sdk_sustainability.types.dimension

        out[aws_sdk_sustainability.types.dimension.deserialize_json(key)] = value
    return out
