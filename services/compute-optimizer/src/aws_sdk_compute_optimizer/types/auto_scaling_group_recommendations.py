"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingGroupRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation

AutoScalingGroupRecommendations: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation.AutoScalingGroupRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingGroupRecommendations) -> list:
    import aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutoScalingGroupRecommendations:
    import aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation

    out: AutoScalingGroupRecommendations = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
