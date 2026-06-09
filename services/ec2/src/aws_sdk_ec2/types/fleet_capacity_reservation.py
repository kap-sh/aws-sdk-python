"""Generated from Smithy shape ``com.amazonaws.ec2#FleetCapacityReservation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.capacity_reservation_instance_platform
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.double_with_constraints
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.integer_with_constraints
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class FleetCapacityReservation(TypedDict):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the Capacity Reservation reserves capacity.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type for which the Capacity Reservation reserves capacity.</p>"""
    instance_platform: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform"
    ]
    """<p>The type of operating system for which the Capacity Reservation reserves capacity.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the Capacity Reservation reserves capacity.</p>"""
    total_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of instances for which the Capacity Reservation reserves capacity.</p>"""
    fulfilled_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The number of capacity units fulfilled by the Capacity Reservation. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity\">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the Capacity Reservation reserves capacity for EBS-optimized instance types.</p>"""
    create_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Reservation was created.</p>"""
    weight: NotRequired[
        "aws_sdk_ec2.types.double_with_constraints.DoubleWithConstraints"
    ]
    """<p>The weight of the instance type in the Capacity Reservation Fleet. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#instance-weight\">Instance type weight</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    priority: NotRequired[
        "aws_sdk_ec2.types.integer_with_constraints.IntegerWithConstraints"
    ]
    """<p>The priority of the instance type in the Capacity Reservation Fleet. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#instance-priority\">Instance type priority</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetCapacityReservation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
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
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "total_instance_count" in value:
        pairs.append(
            (f"{prefix}.TotalInstanceCount", str(value["total_instance_count"]))
        )
    if "fulfilled_capacity" in value:
        pairs.append((f"{prefix}.FulfilledCapacity", str(value["fulfilled_capacity"])))
    if "ebs_optimized" in value:
        pairs.append(
            (f"{prefix}.EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "create_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "weight" in value:
        pairs.append((f"{prefix}.Weight", str(value["weight"])))
    if "priority" in value:
        pairs.append((f"{prefix}.Priority", str(value["priority"])))


def deserialize_ec2_query(el: Element) -> FleetCapacityReservation:
    out: FleetCapacityReservation = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
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
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_total_instance_count = el.find("TotalInstanceCount")
    if child_total_instance_count is not None:
        out["total_instance_count"] = int(child_total_instance_count.text or "")
    child_fulfilled_capacity = el.find("FulfilledCapacity")
    if child_fulfilled_capacity is not None:
        out["fulfilled_capacity"] = float(child_fulfilled_capacity.text or "")
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["create_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_create_date
            )
        )
    child_weight = el.find("Weight")
    if child_weight is not None:
        out["weight"] = float(child_weight.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    return out
