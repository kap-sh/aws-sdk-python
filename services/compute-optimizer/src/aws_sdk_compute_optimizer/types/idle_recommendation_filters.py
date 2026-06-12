"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.idle_recommendation_filter

IdleRecommendationFilters: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.idle_recommendation_filter.IdleRecommendationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendationFilters) -> list:
    import aws_sdk_compute_optimizer.types.idle_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.idle_recommendation_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdleRecommendationFilters:
    import aws_sdk_compute_optimizer.types.idle_recommendation_filter

    out: IdleRecommendationFilters = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.idle_recommendation_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
