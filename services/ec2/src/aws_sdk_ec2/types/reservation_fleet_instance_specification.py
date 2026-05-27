"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationFleetInstanceSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
    """<p>The number of capacity units provided by the specified instance type. This value, together with the total target capacity that you specify for the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity\">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone in which the Capacity Reservation Fleet reserves the capacity. A Capacity Reservation Fleet can't span Availability Zones. All instance type specifications that you specify for the Fleet must use the same Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the Capacity Reservation Fleet reserves the capacity. A Capacity Reservation Fleet can't span Availability Zones. All instance type specifications that you specify for the Fleet must use the same Availability Zone.</p>"""
    ebs_optimized: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the Capacity Reservation Fleet supports EBS-optimized instances types. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using EBS-optimized instance types.</p>"""
    priority: NotRequired[
        "aws_sdk_ec2.types.integer_with_constraints.IntegerWithConstraints"
    ]
    """<p>The priority to assign to the instance type. This value is used to determine which of the instance types specified for the Fleet should be prioritized for use. A lower value indicates a high priority. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#instance-priority\">Instance type priority</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
