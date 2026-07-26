"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.instance_recommendation_option

RecommendationOptions: TypeAlias = list[
    "capo_compute_optimizer.types.instance_recommendation_option.InstanceRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationOptions) -> list:
    import capo_compute_optimizer.types.instance_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.instance_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationOptions:
    import capo_compute_optimizer.types.instance_recommendation_option

    out: RecommendationOptions = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.instance_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out
