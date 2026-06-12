"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnvironmentParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.environment_parameter

EnvironmentParameters: TypeAlias = list[
    "aws_sdk_sagemaker.types.environment_parameter.EnvironmentParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentParameters) -> list:
    import aws_sdk_sagemaker.types.environment_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.environment_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentParameters:
    import aws_sdk_sagemaker.types.environment_parameter

    out: EnvironmentParameters = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.environment_parameter.deserialize_aws_json_1_1(item)
        )
    return out
