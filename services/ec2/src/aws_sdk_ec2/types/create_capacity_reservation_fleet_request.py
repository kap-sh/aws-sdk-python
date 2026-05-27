"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationFleetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.fleet_capacity_reservation_tenancy
    import aws_sdk_ec2.types.fleet_instance_match_criteria
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.reservation_fleet_instance_specification_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateCapacityReservationFleetRequest(TypedDict):
    allocation_strategy: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently, only the <code>prioritized</code> allocation strategy is supported. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy\"> Allocation strategy</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Valid values: <code>prioritized</code> </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensure Idempotency</a>.</p>"""
    instance_type_specifications: NotRequired[
        "aws_sdk_ec2.types.reservation_fleet_instance_specification_list.ReservationFleetInstanceSpecificationList"
    ]
    """<p>Information about the instance types for which to reserve the capacity.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.fleet_capacity_reservation_tenancy.FleetCapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. The Capacity Reservation Fleet can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation Fleet is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservations are created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    total_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity\">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to <code>expired</code> and all of the Capacity Reservations in the Fleet expire.</p> <p>The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify <code>5/31/2019</code>, <code>13:30:55</code>, the Capacity Reservation Fleet is guaranteed to expire between <code>13:30:55</code> and <code>14:30:55</code> on <code>5/31/2019</code>. </p>"""
    instance_match_criteria: NotRequired[
        "aws_sdk_ec2.types.fleet_instance_match_criteria.FleetInstanceMatchCriteria"
    ]
    """<p>Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.</p> <p>Currently, Capacity Reservation Fleets support <code>open</code> instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations in the Fleet.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
