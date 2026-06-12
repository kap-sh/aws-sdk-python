"""Generated from Smithy shape ``com.amazonaws.fis#TargetInformationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.target_information_key
    import aws_sdk_fis.types.target_information_value

TargetInformationMap: TypeAlias = dict[
    "aws_sdk_fis.types.target_information_key.TargetInformationKey",
    "aws_sdk_fis.types.target_information_value.TargetInformationValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TargetInformationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TargetInformationMap:
    out: TargetInformationMap = {}
    for key, value in data.items():
        out[key] = value
    return out
