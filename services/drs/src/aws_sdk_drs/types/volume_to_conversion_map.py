"""Generated from Smithy shape ``com.amazonaws.drs#VolumeToConversionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.conversion_map
    import aws_sdk_drs.types.large_bounded_string

VolumeToConversionMap: TypeAlias = dict[
    "aws_sdk_drs.types.large_bounded_string.LargeBoundedString",
    "aws_sdk_drs.types.conversion_map.ConversionMap",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: VolumeToConversionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_drs.types.conversion_map

        out[key] = aws_sdk_drs.types.conversion_map.serialize_json(value)
    return out


def deserialize_json(data: dict) -> VolumeToConversionMap:
    out: VolumeToConversionMap = {}
    for key, value in data.items():
        import aws_sdk_drs.types.conversion_map

        out[key] = aws_sdk_drs.types.conversion_map.deserialize_json(value)
    return out
