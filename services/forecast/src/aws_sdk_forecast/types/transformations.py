"""Generated from Smithy shape ``com.amazonaws.forecast#Transformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.value

Transformations: TypeAlias = dict[
    "aws_sdk_forecast.types.name.Name", "aws_sdk_forecast.types.value.Value"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Transformations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Transformations:
    out: Transformations = {}
    for key, value in data.items():
        out[key] = value
    return out
