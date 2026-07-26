"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnvironmentParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.environment_parameter

EnvironmentParameters: TypeAlias = list[
    "capo_sagemaker.types.environment_parameter.EnvironmentParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentParameters) -> list:
    import capo_sagemaker.types.environment_parameter

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.environment_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentParameters:
    import capo_sagemaker.types.environment_parameter

    out: EnvironmentParameters = []
    for item in data:
        out.append(
            capo_sagemaker.types.environment_parameter.deserialize_aws_json_1_1(item)
        )
    return out
