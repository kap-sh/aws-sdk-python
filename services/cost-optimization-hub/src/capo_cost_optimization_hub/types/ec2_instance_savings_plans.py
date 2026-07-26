"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2InstanceSavingsPlans``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.ec2_instance_savings_plans_configuration
    import capo_cost_optimization_hub.types.savings_plans_cost_calculation


class Ec2InstanceSavingsPlans(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_cost_optimization_hub.types.ec2_instance_savings_plans_configuration.Ec2InstanceSavingsPlansConfiguration"
    ]
    """<p>The EC2 instance Savings Plans configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "capo_cost_optimization_hub.types.savings_plans_cost_calculation.SavingsPlansCostCalculation"
    ]
    """<p>Cost impact of the Savings Plans purchase recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2InstanceSavingsPlans) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_cost_optimization_hub.types.ec2_instance_savings_plans_configuration

        out["configuration"] = (
            capo_cost_optimization_hub.types.ec2_instance_savings_plans_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import capo_cost_optimization_hub.types.savings_plans_cost_calculation

        out["costCalculation"] = (
            capo_cost_optimization_hub.types.savings_plans_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2InstanceSavingsPlans:
    out: Ec2InstanceSavingsPlans = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import capo_cost_optimization_hub.types.ec2_instance_savings_plans_configuration

        out["configuration"] = (
            capo_cost_optimization_hub.types.ec2_instance_savings_plans_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import capo_cost_optimization_hub.types.savings_plans_cost_calculation

        out["cost_calculation"] = (
            capo_cost_optimization_hub.types.savings_plans_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
