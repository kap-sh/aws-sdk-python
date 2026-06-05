"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateOverrides``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.instance_requirements
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class LaunchTemplateOverrides(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p>"""
    spot_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in which to launch the instances.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which to launch the instances. For example, <code>us-east-2a</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    weighted_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.</p> <p>If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.</p> <note> <p>When specifying weights, the price used in the <code>lowestPrice</code> and <code>priceCapacityOptimized</code> allocation strategies is per <i>unit</i> hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested <code>TargetCapacity</code>, resulting in only 1 instance being launched, the price used is per <i>instance</i> hour.</p> </note>"""
    priority: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The priority for the launch template override. The highest priority is launched first.</p> <p>If <code>OnDemandAllocationStrategy</code> is set to <code>prioritized</code>, Spot Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity.</p> <p>If the Spot <code>AllocationStrategy</code> is set to <code>capacityOptimizedPrioritized</code>, Spot Fleet uses priority on a best-effort basis to determine which launch template override to use in fulfilling Spot capacity, but optimizes for capacity first.</p> <p>Valid values are whole numbers starting at <code>0</code>. The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority. You can set the same priority for different launch template overrides.</p>"""
    instance_requirements: NotRequired[
        "aws_sdk_ec2.types.instance_requirements.InstanceRequirements"
    ]
    """<p>The instance requirements. When you specify instance requirements, Amazon EC2 will identify instance types with the provided requirements, and then use your On-Demand and Spot allocation strategies to launch instances from these instance types, in the same way as when you specify a list of instance types.</p> <note> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>.</p> </note>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone in which to launch the instances. For example, <code>use2-az1</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateOverrides, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "spot_price" in value:
        pairs.append((f"{prefix}.SpotPrice", str(value["spot_price"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "weighted_capacity" in value:
        pairs.append((f"{prefix}.WeightedCapacity", str(value["weighted_capacity"])))
    if "priority" in value:
        pairs.append((f"{prefix}.Priority", str(value["priority"])))
    if "instance_requirements" in value:
        import aws_sdk_ec2.types.instance_requirements

        aws_sdk_ec2.types.instance_requirements.serialize_ec2_query(
            value["instance_requirements"], pairs, f"{prefix}.InstanceRequirements"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateOverrides:
    out: LaunchTemplateOverrides = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_spot_price = el.find("SpotPrice")
    if child_spot_price is not None:
        out["spot_price"] = str(child_spot_price.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_weighted_capacity = el.find("WeightedCapacity")
    if child_weighted_capacity is not None:
        out["weighted_capacity"] = float(child_weighted_capacity.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = float(child_priority.text or "")
    child_instance_requirements = el.find("InstanceRequirements")
    if child_instance_requirements is not None:
        import aws_sdk_ec2.types.instance_requirements

        out["instance_requirements"] = (
            aws_sdk_ec2.types.instance_requirements.deserialize_ec2_query(
                child_instance_requirements
            )
        )
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
