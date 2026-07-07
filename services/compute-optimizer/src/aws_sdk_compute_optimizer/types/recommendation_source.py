"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.recommendation_source_arn
    import aws_sdk_compute_optimizer.types.recommendation_source_type


class RecommendationSource(TypedDict, closed=True):
    recommendation_source_arn: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_source_arn.RecommendationSourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the recommendation source.</p>"""
    recommendation_source_type: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_source_type.RecommendationSourceType"
    ]
    """<p>The resource type of the recommendation source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSource) -> dict:
    out: dict = {}
    if "recommendation_source_arn" in value:
        out["recommendationSourceArn"] = value["recommendation_source_arn"]
    if "recommendation_source_type" in value:
        import aws_sdk_compute_optimizer.types.recommendation_source_type

        out["recommendationSourceType"] = (
            aws_sdk_compute_optimizer.types.recommendation_source_type.serialize_aws_json_1_0(
                value["recommendation_source_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationSource:
    out: RecommendationSource = {}  # type: ignore[typeddict-item]
    if "recommendationSourceArn" in data:
        out["recommendation_source_arn"] = data["recommendationSourceArn"]
    if "recommendationSourceType" in data:
        import aws_sdk_compute_optimizer.types.recommendation_source_type

        out["recommendation_source_type"] = (
            aws_sdk_compute_optimizer.types.recommendation_source_type.deserialize_aws_json_1_0(
                data["recommendationSourceType"]
            )
        )
    return out
