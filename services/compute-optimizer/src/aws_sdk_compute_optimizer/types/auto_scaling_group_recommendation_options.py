"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AutoScalingGroupRecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation_option

AutoScalingGroupRecommendationOptions: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation_option.AutoScalingGroupRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingGroupRecommendationOptions) -> list:
    import aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutoScalingGroupRecommendationOptions:
    import aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation_option

    out: AutoScalingGroupRecommendationOptions = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.auto_scaling_group_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out
