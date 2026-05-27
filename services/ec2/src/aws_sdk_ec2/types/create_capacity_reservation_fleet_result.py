"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationFleetResult``."""

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


class CreateCapacityReservationFleetResult(TypedDict):
    capacity_reservation_fleet_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
    ]
    """<p>The ID of the Capacity Reservation Fleet.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_state.CapacityReservationFleetState"
    ]
    """<p>The status of the Capacity Reservation Fleet.</p>"""
    total_target_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of capacity units for which the Capacity Reservation Fleet reserves capacity.</p>"""
    total_fulfilled_capacity: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The requested capacity units that have been successfully reserved.</p>"""
    instance_match_criteria: NotRequired[
        "aws_sdk_ec2.types.fleet_instance_match_criteria.FleetInstanceMatchCriteria"
    ]
    """<p>The instance matching criteria for the Capacity Reservation Fleet.</p>"""
    allocation_strategy: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation strategy used by the Capacity Reservation Fleet.</p>"""
    create_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the Capacity Reservation Fleet was created.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time at which the Capacity Reservation Fleet expires.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.fleet_capacity_reservation_tenancy.FleetCapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of Capacity Reservation Fleet.</p>"""
    fleet_capacity_reservations: NotRequired[
        "aws_sdk_ec2.types.fleet_capacity_reservation_set.FleetCapacityReservationSet"
    ]
    """<p>Information about the individual Capacity Reservations in the Capacity Reservation Fleet.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Capacity Reservation Fleet.</p>"""
