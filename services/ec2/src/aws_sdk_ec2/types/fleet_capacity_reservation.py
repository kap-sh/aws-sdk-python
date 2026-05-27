"""Generated from Smithy shape ``com.amazonaws.ec2#FleetCapacityReservation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
