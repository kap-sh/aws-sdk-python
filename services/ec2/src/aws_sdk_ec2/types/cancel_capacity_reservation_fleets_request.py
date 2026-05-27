"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservationFleetsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_fleet_id_set


class CancelCapacityReservationFleetsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    capacity_reservation_fleet_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_id_set.CapacityReservationFleetIdSet"
    ]
    """<p>The IDs of the Capacity Reservation Fleets to cancel.</p>"""
