"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferencesDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.recommendation_preferences_detail

RecommendationPreferencesDetails: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.recommendation_preferences_detail.RecommendationPreferencesDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationPreferencesDetails) -> list:
    import aws_sdk_compute_optimizer.types.recommendation_preferences_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_preferences_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationPreferencesDetails:
    import aws_sdk_compute_optimizer.types.recommendation_preferences_detail

    out: RecommendationPreferencesDetails = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_preferences_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
