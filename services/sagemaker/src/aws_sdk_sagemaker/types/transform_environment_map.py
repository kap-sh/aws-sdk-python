"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformEnvironmentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.transform_environment_key
    import aws_sdk_sagemaker.types.transform_environment_value

TransformEnvironmentMap: TypeAlias = dict[
    "aws_sdk_sagemaker.types.transform_environment_key.TransformEnvironmentKey",
    "aws_sdk_sagemaker.types.transform_environment_value.TransformEnvironmentValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TransformEnvironmentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformEnvironmentMap:
    out: TransformEnvironmentMap = {}
    for key, value in data.items():
        out[key] = value
    return out
