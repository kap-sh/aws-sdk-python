"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferenceNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.recommendation_preference_name

RecommendationPreferenceNames: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.recommendation_preference_name.RecommendationPreferenceName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationPreferenceNames) -> list:
    import aws_sdk_compute_optimizer.types.recommendation_preference_name

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_preference_name.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationPreferenceNames:
    import aws_sdk_compute_optimizer.types.recommendation_preference_name

    out: RecommendationPreferenceNames = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_preference_name.deserialize_aws_json_1_0(
                item
            )
        )
    return out
