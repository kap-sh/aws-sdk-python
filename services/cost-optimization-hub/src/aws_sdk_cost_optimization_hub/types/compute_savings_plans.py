"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ComputeSavingsPlans``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.compute_savings_plans_configuration
    import aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation


class ComputeSavingsPlans(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_cost_optimization_hub.types.compute_savings_plans_configuration.ComputeSavingsPlansConfiguration"
    ]
    """<p>Configuration details of the Compute Savings Plans to purchase.</p>"""
    cost_calculation: NotRequired[
        "aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation.SavingsPlansCostCalculation"
    ]
    """<p>Cost impact of the Savings Plans purchase recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeSavingsPlans) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_cost_optimization_hub.types.compute_savings_plans_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.compute_savings_plans_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation

        out["costCalculation"] = (
            aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ComputeSavingsPlans:
    out: ComputeSavingsPlans = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_cost_optimization_hub.types.compute_savings_plans_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.compute_savings_plans_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation

        out["cost_calculation"] = (
            aws_sdk_cost_optimization_hub.types.savings_plans_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
