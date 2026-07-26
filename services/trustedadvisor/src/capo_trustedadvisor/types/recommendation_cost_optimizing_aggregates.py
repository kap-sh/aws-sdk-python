"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationCostOptimizingAggregates``."""

from typing_extensions import TypedDict

from capo_trustedadvisor.errors import DeserializationError


class RecommendationCostOptimizingAggregates(TypedDict, closed=True):
    estimated_monthly_savings: "float"
    """<p>The estimated monthly savings</p>"""
    estimated_percent_monthly_savings: "float"
    """<p>The estimated percently monthly savings</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationCostOptimizingAggregates) -> dict:
    out: dict = {}
    out["estimatedMonthlySavings"] = value["estimated_monthly_savings"]
    out["estimatedPercentMonthlySavings"] = value["estimated_percent_monthly_savings"]
    return out


def deserialize_json(data: dict) -> RecommendationCostOptimizingAggregates:
    out: RecommendationCostOptimizingAggregates = {}  # type: ignore[typeddict-item]
    if "estimatedMonthlySavings" in data:
        out["estimated_monthly_savings"] = data["estimatedMonthlySavings"]
    else:
        raise DeserializationError(
            "RecommendationCostOptimizingAggregates.estimated_monthly_savings required"
        )
    if "estimatedPercentMonthlySavings" in data:
        out["estimated_percent_monthly_savings"] = data[
            "estimatedPercentMonthlySavings"
        ]
    else:
        raise DeserializationError(
            "RecommendationCostOptimizingAggregates.estimated_percent_monthly_savings required"
        )
    return out
