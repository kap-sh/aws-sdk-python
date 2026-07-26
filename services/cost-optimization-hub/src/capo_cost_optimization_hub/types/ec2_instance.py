"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.ec2_instance_configuration
    import capo_cost_optimization_hub.types.resource_cost_calculation


class Ec2Instance(TypedDict, closed=True):
    configuration: NotRequired[
        "capo_cost_optimization_hub.types.ec2_instance_configuration.Ec2InstanceConfiguration"
    ]
    """<p>The EC2 instance configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "capo_cost_optimization_hub.types.resource_cost_calculation.ResourceCostCalculation"
    ]
    """<p>Cost impact of the recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2Instance) -> dict:
    out: dict = {}
    if "configuration" in value:
        import capo_cost_optimization_hub.types.ec2_instance_configuration

        out["configuration"] = (
            capo_cost_optimization_hub.types.ec2_instance_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import capo_cost_optimization_hub.types.resource_cost_calculation

        out["costCalculation"] = (
            capo_cost_optimization_hub.types.resource_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2Instance:
    out: Ec2Instance = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import capo_cost_optimization_hub.types.ec2_instance_configuration

        out["configuration"] = (
            capo_cost_optimization_hub.types.ec2_instance_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import capo_cost_optimization_hub.types.resource_cost_calculation

        out["cost_calculation"] = (
            capo_cost_optimization_hub.types.resource_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
