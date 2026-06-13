"""Generated from Smithy shape ``com.amazonaws.drs#VolumeToSizeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.large_bounded_string
    import aws_sdk_drs.types.positive_integer

VolumeToSizeMap: TypeAlias = dict[
    "aws_sdk_drs.types.large_bounded_string.LargeBoundedString",
    "aws_sdk_drs.types.positive_integer.PositiveInteger",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: VolumeToSizeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> VolumeToSizeMap:
    out: VolumeToSizeMap = {}
    for key, value in data.items():
        out[key] = value
    return out
