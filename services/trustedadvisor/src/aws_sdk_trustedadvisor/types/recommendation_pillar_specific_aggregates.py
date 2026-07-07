"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationPillarSpecificAggregates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.recommendation_cost_optimizing_aggregates


class RecommendationPillarSpecificAggregates(TypedDict, closed=True):
    cost_optimizing: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_cost_optimizing_aggregates.RecommendationCostOptimizingAggregates"
    ]
    """<p>Cost optimizing aggregates</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationPillarSpecificAggregates) -> dict:
    out: dict = {}
    if "cost_optimizing" in value:
        import aws_sdk_trustedadvisor.types.recommendation_cost_optimizing_aggregates

        out["costOptimizing"] = (
            aws_sdk_trustedadvisor.types.recommendation_cost_optimizing_aggregates.serialize_json(
                value["cost_optimizing"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecommendationPillarSpecificAggregates:
    out: RecommendationPillarSpecificAggregates = {}  # type: ignore[typeddict-item]
    if "costOptimizing" in data:
        import aws_sdk_trustedadvisor.types.recommendation_cost_optimizing_aggregates

        out["cost_optimizing"] = (
            aws_sdk_trustedadvisor.types.recommendation_cost_optimizing_aggregates.deserialize_json(
                data["costOptimizing"]
            )
        )
    return out
