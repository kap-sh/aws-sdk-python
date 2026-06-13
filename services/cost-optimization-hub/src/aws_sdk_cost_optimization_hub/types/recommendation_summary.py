"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RecommendationSummary``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RecommendationSummary(TypedDict):
    group: NotRequired["str"]
    """<p>The grouping of recommendations.</p>"""
    estimated_monthly_savings: NotRequired["float"]
    """<p>The estimated total savings resulting from modifications, on a monthly basis.</p>"""
    recommendation_count: NotRequired["int"]
    """<p>The total number of instance recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSummary) -> dict:
    out: dict = {}
    if "group" in value:
        out["group"] = value["group"]
    if "estimated_monthly_savings" in value:
        out["estimatedMonthlySavings"] = value["estimated_monthly_savings"]
    if "recommendation_count" in value:
        out["recommendationCount"] = value["recommendation_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationSummary:
    out: RecommendationSummary = {}  # type: ignore[typeddict-item]
    if "group" in data:
        out["group"] = data["group"]
    if "estimatedMonthlySavings" in data:
        out["estimated_monthly_savings"] = data["estimatedMonthlySavings"]
    if "recommendationCount" in data:
        out["recommendation_count"] = data["recommendationCount"]
    return out
