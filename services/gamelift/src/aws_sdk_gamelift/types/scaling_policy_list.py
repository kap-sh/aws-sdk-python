"""Generated from Smithy shape ``com.amazonaws.gamelift#ScalingPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.scaling_policy

ScalingPolicyList: TypeAlias = list[
    "aws_sdk_gamelift.types.scaling_policy.ScalingPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicyList) -> list:
    import aws_sdk_gamelift.types.scaling_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.scaling_policy.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ScalingPolicyList:
    import aws_sdk_gamelift.types.scaling_policy

    out: ScalingPolicyList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.scaling_policy.deserialize_aws_json_1_1(item))
    return out
