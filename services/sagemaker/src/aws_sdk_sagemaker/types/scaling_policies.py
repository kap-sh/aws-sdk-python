"""Generated from Smithy shape ``com.amazonaws.sagemaker#ScalingPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.scaling_policy

ScalingPolicies: TypeAlias = list[
    "aws_sdk_sagemaker.types.scaling_policy.ScalingPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicies) -> list:
    import aws_sdk_sagemaker.types.scaling_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.scaling_policy.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingPolicies:
    import aws_sdk_sagemaker.types.scaling_policy

    out: ScalingPolicies = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.scaling_policy.deserialize_aws_json_1_1(item)
        )
    return out
