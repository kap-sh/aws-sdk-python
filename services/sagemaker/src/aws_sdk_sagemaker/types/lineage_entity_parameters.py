"""Generated from Smithy shape ``com.amazonaws.sagemaker#LineageEntityParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string_parameter_value

LineageEntityParameters: TypeAlias = dict[
    "aws_sdk_sagemaker.types.string_parameter_value.StringParameterValue",
    "aws_sdk_sagemaker.types.string_parameter_value.StringParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LineageEntityParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LineageEntityParameters:
    out: LineageEntityParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
