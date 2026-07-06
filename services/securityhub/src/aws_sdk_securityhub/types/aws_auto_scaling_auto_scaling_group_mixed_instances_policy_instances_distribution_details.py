"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails(
    TypedDict, closed=True
):
    on_demand_allocation_strategy: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>How to allocate instance types to fulfill On-Demand capacity. The valid value is <code>prioritized</code>.</p>"""
    on_demand_base_capacity: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The minimum amount of the Auto Scaling group's capacity that must be fulfilled by On-Demand Instances.</p>"""
    on_demand_percentage_above_base_capacity: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p>The percentage of On-Demand Instances and Spot Instances for additional capacity beyond <code>OnDemandBaseCapacity</code>.</p>"""
    spot_allocation_strategy: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>How to allocate instances across Spot Instance pools. Valid values are as follows:</p> <ul> <li> <p> <code>lowest-price</code> </p> </li> <li> <p> <code>capacity-optimized</code> </p> </li> <li> <p> <code>capacity-optimized-prioritized</code> </p> </li> </ul>"""
    spot_instance_pools: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of Spot Instance pools across which to allocate your Spot Instances.</p>"""
    spot_max_price: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails,
) -> dict:
    out: dict = {}
    if "on_demand_allocation_strategy" in value:
        out["OnDemandAllocationStrategy"] = value["on_demand_allocation_strategy"]
    if "on_demand_base_capacity" in value:
        out["OnDemandBaseCapacity"] = value["on_demand_base_capacity"]
    if "on_demand_percentage_above_base_capacity" in value:
        out["OnDemandPercentageAboveBaseCapacity"] = value[
            "on_demand_percentage_above_base_capacity"
        ]
    if "spot_allocation_strategy" in value:
        out["SpotAllocationStrategy"] = value["spot_allocation_strategy"]
    if "spot_instance_pools" in value:
        out["SpotInstancePools"] = value["spot_instance_pools"]
    if "spot_max_price" in value:
        out["SpotMaxPrice"] = value["spot_max_price"]
    return out


def deserialize_json(
    data: dict,
) -> AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails:
    out: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails = {}  # type: ignore[typeddict-item]
    if "OnDemandAllocationStrategy" in data:
        out["on_demand_allocation_strategy"] = data["OnDemandAllocationStrategy"]
    if "OnDemandBaseCapacity" in data:
        out["on_demand_base_capacity"] = data["OnDemandBaseCapacity"]
    if "OnDemandPercentageAboveBaseCapacity" in data:
        out["on_demand_percentage_above_base_capacity"] = data[
            "OnDemandPercentageAboveBaseCapacity"
        ]
    if "SpotAllocationStrategy" in data:
        out["spot_allocation_strategy"] = data["SpotAllocationStrategy"]
    if "SpotInstancePools" in data:
        out["spot_instance_pools"] = data["SpotInstancePools"]
    if "SpotMaxPrice" in data:
        out["spot_max_price"] = data["SpotMaxPrice"]
    return out
