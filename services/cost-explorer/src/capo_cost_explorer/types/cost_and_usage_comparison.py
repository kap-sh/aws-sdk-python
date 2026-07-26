"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAndUsageComparison``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.comparison_metrics
    import capo_cost_explorer.types.expression


class CostAndUsageComparison(TypedDict, closed=True):
    cost_and_usage_selector: NotRequired[
        "capo_cost_explorer.types.expression.Expression"
    ]
    metrics: NotRequired[
        "capo_cost_explorer.types.comparison_metrics.ComparisonMetrics"
    ]
    """<p>A mapping of metric names to their comparison values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAndUsageComparison) -> dict:
    out: dict = {}
    if "cost_and_usage_selector" in value:
        import capo_cost_explorer.types.expression

        out["CostAndUsageSelector"] = (
            capo_cost_explorer.types.expression.serialize_aws_json_1_1(
                value["cost_and_usage_selector"]
            )
        )
    if "metrics" in value:
        import capo_cost_explorer.types.comparison_metrics

        out["Metrics"] = (
            capo_cost_explorer.types.comparison_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostAndUsageComparison:
    out: CostAndUsageComparison = {}  # type: ignore[typeddict-item]
    if "CostAndUsageSelector" in data:
        import capo_cost_explorer.types.expression

        out["cost_and_usage_selector"] = (
            capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
                data["CostAndUsageSelector"]
            )
        )
    if "Metrics" in data:
        import capo_cost_explorer.types.comparison_metrics

        out["metrics"] = (
            capo_cost_explorer.types.comparison_metrics.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    return out
