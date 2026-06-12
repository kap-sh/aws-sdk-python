"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.recommendation_summary

RecommendationSummaries: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.recommendation_summary.RecommendationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSummaries) -> list:
    import aws_sdk_compute_optimizer.types.recommendation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationSummaries:
    import aws_sdk_compute_optimizer.types.recommendation_summary

    out: RecommendationSummaries = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
