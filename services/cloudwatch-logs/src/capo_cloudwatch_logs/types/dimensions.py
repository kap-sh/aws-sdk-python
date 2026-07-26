"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Dimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.dimensions_key
    import capo_cloudwatch_logs.types.dimensions_value

Dimensions: TypeAlias = dict[
    "capo_cloudwatch_logs.types.dimensions_key.DimensionsKey",
    "capo_cloudwatch_logs.types.dimensions_value.DimensionsValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Dimensions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Dimensions:
    out: Dimensions = {}
    for key, value in data.items():
        out[key] = value
    return out
