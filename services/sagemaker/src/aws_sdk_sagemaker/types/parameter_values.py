"""Generated from Smithy shape ``com.amazonaws.sagemaker#ParameterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parameter_value

ParameterValues: TypeAlias = list[
    "aws_sdk_sagemaker.types.parameter_value.ParameterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ParameterValues:
    return list(data)
