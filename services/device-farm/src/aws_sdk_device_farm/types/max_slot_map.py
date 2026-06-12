"""Generated from Smithy shape ``com.amazonaws.devicefarm#MaxSlotMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.integer
    import aws_sdk_device_farm.types.string

MaxSlotMap: TypeAlias = dict[
    "aws_sdk_device_farm.types.string.String",
    "aws_sdk_device_farm.types.integer.Integer",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: MaxSlotMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> MaxSlotMap:
    out: MaxSlotMap = {}
    for key, value in data.items():
        out[key] = value
    return out
