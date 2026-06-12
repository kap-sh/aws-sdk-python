"""Generated from Smithy shape ``com.amazonaws.forecast#FeaturizationMethodParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.parameter_key
    import aws_sdk_forecast.types.parameter_value

FeaturizationMethodParameters: TypeAlias = dict[
    "aws_sdk_forecast.types.parameter_key.ParameterKey",
    "aws_sdk_forecast.types.parameter_value.ParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FeaturizationMethodParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturizationMethodParameters:
    out: FeaturizationMethodParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
