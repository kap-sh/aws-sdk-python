"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferencesDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.recommendation_preferences_detail

RecommendationPreferencesDetails: TypeAlias = list[
    "capo_compute_optimizer.types.recommendation_preferences_detail.RecommendationPreferencesDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationPreferencesDetails) -> list:
    import capo_compute_optimizer.types.recommendation_preferences_detail

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.recommendation_preferences_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationPreferencesDetails:
    import capo_compute_optimizer.types.recommendation_preferences_detail

    out: RecommendationPreferencesDetails = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.recommendation_preferences_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
