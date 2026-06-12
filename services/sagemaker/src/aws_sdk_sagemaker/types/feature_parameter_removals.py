"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureParameterRemovals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_parameter_key

FeatureParameterRemovals: TypeAlias = list[
    "aws_sdk_sagemaker.types.feature_parameter_key.FeatureParameterKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureParameterRemovals) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FeatureParameterRemovals:
    return list(data)
