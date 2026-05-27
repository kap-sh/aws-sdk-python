"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleet``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_id
    import aws_sdk_ec2.types.capacity_reservation_fleet_state
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.fleet_capacity_reservation_set
    import aws_sdk_ec2.types.fleet_capacity_reservation_tenancy
    import aws_sdk_ec2.types.fleet_instance_match_criteria
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class CapacityReservationFleet(TypedDict):
    capacity_reservation_fleet_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
    ]
    """<p>The ID of the Capacity Reservation Fleet.</p>"""
    capacity_reservation_fleet_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the Capacity Reservation Fleet.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_state.CapacityReservationFleetState"
    ]
    """<p>The state of the Capacity Reservation Fleet. Possible states include:</p> <ul> <li> <p> <code>submitted</code> - The Capacity Reservation Fleet request has been submitted and Amazon Elastic Compute Cloud is preparing to create the Capacity Reservations.</p> </li> <li> <p> <code>modifying</code> - The Capacity Reservation Fleet is being modified. The Fleet remains in this state until the modification is complete.</p> </li> <li> <p> <code>active</code> - The Capacity Reservation Fleet has fulfilled its total target capacity and it is attempting to maintain this capacity. The Fleet remains in this state until it is modified or deleted.</p> </li> <li> <p> <code>partially_fulfilled</code> - The Capacity Reservation Fleet has partially fulfilled its total target capacity. There is insufficient Amazon EC2 to fulfill the total target capacity. The Fleet is attempting to asynchronously fulfill its total target capacity.</p> </li> <li> <p> <code>expiring</code> - The Capacity Reservation Fleet has reach its end date and it is in the process of expiring. One or more of its Capacity reservations might still be active.</p> </li> <li> <p> <code>expired</code> - The Capacity Reservation Fleet has reach its end date. The Fleet and its Capacity Reservations are expired. The Fleet can't create new Capacity Reservations.</p> </li> <li> <p> <code>cancelling</code> - The Capacity Reservation Fleet is in the process of being cancelled. One or more of its Capacity reservations might still be active.</p> </li> <li> <p> <code>cancelled</code> - The Capacity Reservation Fleet has been manually cancelled. The Fleet and its Capacity Reservations are cancelled and the Fleet can't create new Capacity Reservations.</p> </li> <li> <p> <code>failed</code> - The Capacity Reservation Fleet failed to reserve capacity for the specified instance types.</p> </li> </ul>"""
    total_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of capacity units for which the Capacity Reservation Fleet reserves capacity. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity\">Total target capacity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    total_fulfilled_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The capacity units that have been fulfilled.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.fleet_capacity_reservation_tenancy.FleetCapacityReservationTenancy"
    ]
    """<p>The tenancy of the Capacity Reservation Fleet. Tenancies include:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation Fleet is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservation Fleet is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Reservation Fleet expires.</p>"""
    create_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Reservation Fleet was created.</p>"""
    instance_match_criteria: NotRequired[
        "aws_sdk_ec2.types.fleet_instance_match_criteria.FleetInstanceMatchCriteria"
    ]
    """<p>Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.</p> <p>Currently, Capacity Reservation Fleets support <code>open</code> instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.</p>"""
    allocation_strategy: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. For more information, see For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy\">Allocation strategy</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_type_specifications: NotRequired[
        "aws_sdk_ec2.types.fleet_capacity_reservation_set.FleetCapacityReservationSet"
    ]
    """<p>Information about the instance types for which to reserve the capacity.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Capacity Reservation Fleet.</p>"""
