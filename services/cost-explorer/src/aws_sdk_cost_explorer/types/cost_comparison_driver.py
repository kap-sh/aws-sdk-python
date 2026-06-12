"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostComparisonDriver``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.comparison_metrics
    import aws_sdk_cost_explorer.types.cost_drivers
    import aws_sdk_cost_explorer.types.expression


class CostComparisonDriver(TypedDict):
    cost_selector: NotRequired["aws_sdk_cost_explorer.types.expression.Expression"]
    metrics: NotRequired[
        "aws_sdk_cost_explorer.types.comparison_metrics.ComparisonMetrics"
    ]
    """<p>A mapping of metric names to their comparison values.</p>"""
    cost_drivers: NotRequired["aws_sdk_cost_explorer.types.cost_drivers.CostDrivers"]
    """<p>An array of cost drivers, each representing a cost difference between the baseline and comparison time periods. Each entry also includes a metric delta (for example, usage change) that contributed to the cost variance, along with the identifier and type of change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostComparisonDriver) -> dict:
    out: dict = {}
    if "cost_selector" in value:
        import aws_sdk_cost_explorer.types.expression

        out["CostSelector"] = (
            aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
                value["cost_selector"]
            )
        )
    if "metrics" in value:
        import aws_sdk_cost_explorer.types.comparison_metrics

        out["Metrics"] = (
            aws_sdk_cost_explorer.types.comparison_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "cost_drivers" in value:
        import aws_sdk_cost_explorer.types.cost_drivers

        out["CostDrivers"] = (
            aws_sdk_cost_explorer.types.cost_drivers.serialize_aws_json_1_1(
                value["cost_drivers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostComparisonDriver:
    out: CostComparisonDriver = {}  # type: ignore[typeddict-item]
    if "CostSelector" in data:
        import aws_sdk_cost_explorer.types.expression

        out["cost_selector"] = (
            aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
                data["CostSelector"]
            )
        )
    if "Metrics" in data:
        import aws_sdk_cost_explorer.types.comparison_metrics

        out["metrics"] = (
            aws_sdk_cost_explorer.types.comparison_metrics.deserialize_aws_json_1_1(
                data["Metrics"]
            )
        )
    if "CostDrivers" in data:
        import aws_sdk_cost_explorer.types.cost_drivers

        out["cost_drivers"] = (
            aws_sdk_cost_explorer.types.cost_drivers.deserialize_aws_json_1_1(
                data["CostDrivers"]
            )
        )
    return out
