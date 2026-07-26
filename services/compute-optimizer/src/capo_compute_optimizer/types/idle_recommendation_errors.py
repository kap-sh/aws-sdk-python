"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleRecommendationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_recommendation_error

IdleRecommendationErrors: TypeAlias = list[
    "capo_compute_optimizer.types.idle_recommendation_error.IdleRecommendationError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleRecommendationErrors) -> list:
    import capo_compute_optimizer.types.idle_recommendation_error

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.idle_recommendation_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdleRecommendationErrors:
    import capo_compute_optimizer.types.idle_recommendation_error

    out: IdleRecommendationErrors = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.idle_recommendation_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
