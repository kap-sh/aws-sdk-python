"""Generated from Smithy shape ``com.amazonaws.iot#DetailsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.details_key
    import aws_sdk_iot.types.details_value

DetailsMap: TypeAlias = dict[
    "aws_sdk_iot.types.details_key.DetailsKey",
    "aws_sdk_iot.types.details_value.DetailsValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DetailsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> DetailsMap:
    out: DetailsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
