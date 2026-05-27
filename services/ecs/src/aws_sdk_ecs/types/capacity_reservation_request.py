"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityReservationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_reservation_preference
    import aws_sdk_ecs.types.string


class CapacityReservationRequest(TypedDict):
    reservation_group_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the Capacity Reservation resource group in which to run the instance.</p>"""
    reservation_preference: NotRequired[
        "aws_sdk_ecs.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p>The preference on when capacity reservations should be used.</p> <p>Valid values are:</p> <ul> <li> <p> <code>RESERVATIONS_ONLY</code> - Exclusively launch instances into capacity reservations that match the instance requirements configured for the capacity provider. If none exist, instances will fail to provision.</p> </li> <li> <p> <code>RESERVATIONS_FIRST</code> - Prefer to launch instances into a capacity reservation if any exist that match the instance requirements configured for the capacity provider. If none exist, fall back to launching instances On-Demand.</p> </li> <li> <p> <code>RESERVATIONS_EXCLUDED</code> - Avoid using capacity reservations and launch exclusively On-Demand.</p> </li> </ul>"""
