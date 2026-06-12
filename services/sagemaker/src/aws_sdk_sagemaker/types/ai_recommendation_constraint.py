"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationConstraint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_metric


class AIRecommendationConstraint(TypedDict):
    metric: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_metric.AIRecommendationMetric"
    ]
    """<p>The performance metric. Valid values are <code>ttft-ms</code> (time to first token in milliseconds), <code>throughput</code>, and <code>cost</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationConstraint) -> dict:
    out: dict = {}
    if "metric" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_metric

        out["Metric"] = (
            aws_sdk_sagemaker.types.ai_recommendation_metric.serialize_aws_json_1_1(
                value["metric"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationConstraint:
    out: AIRecommendationConstraint = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_metric

        out["metric"] = (
            aws_sdk_sagemaker.types.ai_recommendation_metric.deserialize_aws_json_1_1(
                data["Metric"]
            )
        )
    return out
