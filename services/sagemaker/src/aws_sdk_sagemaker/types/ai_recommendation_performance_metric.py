"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationPerformanceMetric``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string


class AIRecommendationPerformanceMetric(TypedDict):
    metric: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name of the performance metric.</p>"""
    stat: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The statistical measure for the metric.</p>"""
    value: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The value of the metric.</p>"""
    unit: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The unit of the metric value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationPerformanceMetric) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "stat" in value:
        out["Stat"] = value["stat"]
    if "value" in value:
        out["Value"] = value["value"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationPerformanceMetric:
    out: AIRecommendationPerformanceMetric = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        out["metric"] = data["Metric"]
    if "Stat" in data:
        out["stat"] = data["Stat"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Unit" in data:
        out["unit"] = data["Unit"]
    return out
