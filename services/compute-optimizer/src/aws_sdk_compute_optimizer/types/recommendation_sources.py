"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.recommendation_source

RecommendationSources: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.recommendation_source.RecommendationSource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSources) -> list:
    import aws_sdk_compute_optimizer.types.recommendation_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_source.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationSources:
    import aws_sdk_compute_optimizer.types.recommendation_source

    out: RecommendationSources = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.recommendation_source.deserialize_aws_json_1_0(
                item
            )
        )
    return out
