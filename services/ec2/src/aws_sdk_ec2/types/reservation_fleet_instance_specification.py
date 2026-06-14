"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationFleetInstanceSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_instance_platform
    import aws_sdk_ec2.types.double_with_constraints
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.integer_with_constraints
    import aws_sdk_ec2.types.string


class ReservationFleetInstanceSpecification(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type for which the Capacity Reservation Fleet reserves capacity.</p>"""
    instance_platform: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform"
    ]
    """<p>The type of operating system for which the Capacity Reservation Fleet reserves capacity.</p>"""
    weight: NotRequired[
        "aws_sdk_ec2.types.double_with_constraints.DoubleWithConstraints"
    ]
    r"""<p>The number of capacity units provided by the specified instance type. This value, together with the total target capacity that you specify for the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity\">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the Capacity Reservation Fleet reserves the capacity. A Capacity Reservation Fleet can't span Availability Zones. All instance type specifications that you specify for the Fleet must use the same Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the Capacity Reservation Fleet reserves the capacity. A Capacity Reservation Fleet can't span Availability Zones. All instance type specifications that you specify for the Fleet must use the same Availability Zone.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the Capacity Reservation Fleet supports EBS-optimized instances types. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using EBS-optimized instance types.</p>"""
    priority: NotRequired[
        "aws_sdk_ec2.types.integer_with_constraints.IntegerWithConstraints"
    ]
    r"""<p>The priority to assign to the instance type. This value is used to determine which of the instance types specified for the Fleet should be prioritized for use. A lower value indicates a high priority. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#instance-priority\">Instance type priority</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservationFleetInstanceSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_type" in value:
        import aws_sdk_ec2.types.instance_type

        aws_sdk_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{prefix}.InstanceType"
        )
    if "instance_platform" in value:
        import aws_sdk_ec2.types.capacity_reservation_instance_platform

        aws_sdk_ec2.types.capacity_reservation_instance_platform.serialize_ec2_query(
            value["instance_platform"], pairs, f"{prefix}.InstancePlatform"
        )
    if "weight" in value:
        pairs.append((f"{prefix}.Weight", str(value["weight"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{prefix}.EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "priority" in value:
        pairs.append((f"{prefix}.Priority", str(value["priority"])))


def deserialize_ec2_query(el: Element) -> ReservationFleetInstanceSpecification:
    out: ReservationFleetInstanceSpecification = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import aws_sdk_ec2.types.instance_type

        out["instance_type"] = aws_sdk_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_instance_platform = el.find("InstancePlatform")
    if child_instance_platform is not None:
        import aws_sdk_ec2.types.capacity_reservation_instance_platform

        out["instance_platform"] = (
            aws_sdk_ec2.types.capacity_reservation_instance_platform.deserialize_ec2_query(
                child_instance_platform
            )
        )
    child_weight = el.find("Weight")
    if child_weight is not None:
        out["weight"] = float(child_weight.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    return out
