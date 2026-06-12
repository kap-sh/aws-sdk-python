"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobEnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.non_empty_string256
    import aws_sdk_sagemaker.types.string256

OptimizationJobEnvironmentVariables: TypeAlias = dict[
    "aws_sdk_sagemaker.types.non_empty_string256.NonEmptyString256",
    "aws_sdk_sagemaker.types.string256.String256",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: OptimizationJobEnvironmentVariables,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationJobEnvironmentVariables:
    out: OptimizationJobEnvironmentVariables = {}
    for key, value in data.items():
        out[key] = value
    return out
