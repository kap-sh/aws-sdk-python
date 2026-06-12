"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.string128
    import aws_sdk_iotdeviceadvisor.types.string256

TagMap: TypeAlias = dict[
    "aws_sdk_iotdeviceadvisor.types.string128.String128",
    "aws_sdk_iotdeviceadvisor.types.string256.String256",
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
