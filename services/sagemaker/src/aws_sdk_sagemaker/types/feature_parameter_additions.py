"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureParameterAdditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_parameter

FeatureParameterAdditions: TypeAlias = list[
    "aws_sdk_sagemaker.types.feature_parameter.FeatureParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureParameterAdditions) -> list:
    import aws_sdk_sagemaker.types.feature_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.feature_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FeatureParameterAdditions:
    import aws_sdk_sagemaker.types.feature_parameter

    out: FeatureParameterAdditions = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.feature_parameter.deserialize_aws_json_1_1(item)
        )
    return out
