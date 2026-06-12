"""Generated from Smithy shape ``com.amazonaws.iot#AdditionalParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.attribute_key
    import aws_sdk_iot.types.value

AdditionalParameterMap: TypeAlias = dict[
    "aws_sdk_iot.types.attribute_key.AttributeKey", "aws_sdk_iot.types.value.Value"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdditionalParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AdditionalParameterMap:
    out: AdditionalParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
