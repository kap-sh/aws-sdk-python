"""Generated from Smithy shape ``com.amazonaws.sesv2#Dimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.metric_dimension_name
    import aws_sdk_sesv2.types.metric_dimension_value

Dimensions: TypeAlias = dict[
    "aws_sdk_sesv2.types.metric_dimension_name.MetricDimensionName",
    "aws_sdk_sesv2.types.metric_dimension_value.MetricDimensionValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Dimensions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_sesv2.types.metric_dimension_name

        out[aws_sdk_sesv2.types.metric_dimension_name.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> Dimensions:
    out: Dimensions = {}
    for key, value in data.items():
        import aws_sdk_sesv2.types.metric_dimension_name

        out[aws_sdk_sesv2.types.metric_dimension_name.deserialize_json(key)] = value
    return out
