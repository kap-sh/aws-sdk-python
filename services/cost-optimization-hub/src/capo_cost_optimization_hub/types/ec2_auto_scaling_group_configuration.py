"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#Ec2AutoScalingGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.allocation_strategy
    import capo_cost_optimization_hub.types.ec2_auto_scaling_group_type
    import capo_cost_optimization_hub.types.instance_configuration
    import capo_cost_optimization_hub.types.mixed_instance_configuration_list


class Ec2AutoScalingGroupConfiguration(TypedDict, closed=True):
    instance: NotRequired[
        "capo_cost_optimization_hub.types.instance_configuration.InstanceConfiguration"
    ]
    """<p>Details about the instance for the EC2 Auto Scaling group with a single instance type.</p>"""
    mixed_instances: NotRequired[
        "capo_cost_optimization_hub.types.mixed_instance_configuration_list.MixedInstanceConfigurationList"
    ]
    """<p>A list of instance types for an EC2 Auto Scaling group with mixed instance types.</p>"""
    type: NotRequired[
        "capo_cost_optimization_hub.types.ec2_auto_scaling_group_type.Ec2AutoScalingGroupType"
    ]
    """<p>The type of EC2 Auto Scaling group, showing whether it consists of a single instance type or mixed instance types.</p>"""
    allocation_strategy: NotRequired[
        "capo_cost_optimization_hub.types.allocation_strategy.AllocationStrategy"
    ]
    """<p>The strategy used for allocating instances, based on a predefined priority order or based on the lowest available price.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2AutoScalingGroupConfiguration) -> dict:
    out: dict = {}
    if "instance" in value:
        import capo_cost_optimization_hub.types.instance_configuration

        out["instance"] = (
            capo_cost_optimization_hub.types.instance_configuration.serialize_aws_json_1_0(
                value["instance"]
            )
        )
    if "mixed_instances" in value:
        import capo_cost_optimization_hub.types.mixed_instance_configuration_list

        out["mixedInstances"] = (
            capo_cost_optimization_hub.types.mixed_instance_configuration_list.serialize_aws_json_1_0(
                value["mixed_instances"]
            )
        )
    if "type" in value:
        import capo_cost_optimization_hub.types.ec2_auto_scaling_group_type

        out["type"] = (
            capo_cost_optimization_hub.types.ec2_auto_scaling_group_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "allocation_strategy" in value:
        import capo_cost_optimization_hub.types.allocation_strategy

        out["allocationStrategy"] = (
            capo_cost_optimization_hub.types.allocation_strategy.serialize_aws_json_1_0(
                value["allocation_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2AutoScalingGroupConfiguration:
    out: Ec2AutoScalingGroupConfiguration = {}  # type: ignore[typeddict-item]
    if "instance" in data:
        import capo_cost_optimization_hub.types.instance_configuration

        out["instance"] = (
            capo_cost_optimization_hub.types.instance_configuration.deserialize_aws_json_1_0(
                data["instance"]
            )
        )
    if "mixedInstances" in data:
        import capo_cost_optimization_hub.types.mixed_instance_configuration_list

        out["mixed_instances"] = (
            capo_cost_optimization_hub.types.mixed_instance_configuration_list.deserialize_aws_json_1_0(
                data["mixedInstances"]
            )
        )
    if "type" in data:
        import capo_cost_optimization_hub.types.ec2_auto_scaling_group_type

        out["type"] = (
            capo_cost_optimization_hub.types.ec2_auto_scaling_group_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    if "allocationStrategy" in data:
        import capo_cost_optimization_hub.types.allocation_strategy

        out["allocation_strategy"] = (
            capo_cost_optimization_hub.types.allocation_strategy.deserialize_aws_json_1_0(
                data["allocationStrategy"]
            )
        )
    return out
