"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostAndUsageComparison``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.comparison_metrics
    import aws_sdk_cost_explorer.types.expression


class CostAndUsageComparison(TypedDict, closed=True):
    cost_and_usage_selector: NotRequired[
        "aws_sdk_cost_explorer.types.expression.Expression"
    ]
    metrics: NotRequired[
        "aws_sdk_cost_explorer.types.comparison_metrics.ComparisonMetrics"
    ]
    """<p>A mapping of metric names to their comparison values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostAndUsageComparison) -> dict:
    out: dict = {}
    if "cost_and_usage_selector" in value:
        import aws_sdk_cost_explorer.types.expression

        out["CostAndUsageSelector"] = (
            aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
                value["cost_and_usage_selector"]
            )
        )
    if "metrics" in value:
        import aws_sdk_cost_explorer.types.comparison_metrics

        out["Metrics"] = (
            aws_sdk_cost_explorer.types.comparison_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostAndUsageComparison:
    out: CostAndUsageComparison = {}  # type: ignore[typeddict-item]
    if "CostAndUsageSelector" in data:
        import aws_sdk_cost_explorer.types.expression

        out["cost_and_usage_selector"] = (
            aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
                data["CostAndUsageSelector"]
            )
        )
    if "Metrics" in data:
        import aws_sdk_cost_explorer.types.comparison_metrics

        out["metrics"] = (
            aws_sdk_cost_explorer.types.comparison_metrics.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    return out
