"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2AutoScalingGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group_configuration
    import aws_sdk_cost_optimization_hub.types.resource_cost_calculation


class Ec2AutoScalingGroup(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group_configuration.Ec2AutoScalingGroupConfiguration"
    ]
    """<p>The EC2 Auto Scaling group configuration used for recommendations.</p>"""
    cost_calculation: NotRequired[
        "aws_sdk_cost_optimization_hub.types.resource_cost_calculation.ResourceCostCalculation"
    ]
    """<p>Cost impact of the recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2AutoScalingGroup) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "cost_calculation" in value:
        import aws_sdk_cost_optimization_hub.types.resource_cost_calculation

        out["costCalculation"] = (
            aws_sdk_cost_optimization_hub.types.resource_cost_calculation.serialize_aws_json_1_0(
                value["cost_calculation"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2AutoScalingGroup:
    out: Ec2AutoScalingGroup = {}  # type: ignore[typeddict-item]
    if "configuration" in data:
        import aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group_configuration

        out["configuration"] = (
            aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if "costCalculation" in data:
        import aws_sdk_cost_optimization_hub.types.resource_cost_calculation

        out["cost_calculation"] = (
            aws_sdk_cost_optimization_hub.types.resource_cost_calculation.deserialize_aws_json_1_0(
                data["costCalculation"]
            )
        )
    return out
