"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateCapacityReservationSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_preference
    import aws_sdk_ec2.types.capacity_reservation_target


class LaunchTemplateCapacityReservationSpecificationRequest(TypedDict):
    capacity_reservation_preference: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_preference.CapacityReservationPreference"
    ]
    """<p>Indicates the instance's Capacity Reservation preferences. Possible preferences include:</p> <ul> <li> <p> <code>capacity-reservations-only</code> - The instance will only run in a Capacity Reservation or Capacity Reservation group. If capacity isn't available, the instance will fail to launch.</p> </li> <li> <p> <code>open</code> - The instance can run in any <code>open</code> Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, tenancy).</p> </li> <li> <p> <code>none</code> - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity.</p> </li> </ul>"""
    capacity_reservation_target: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_target.CapacityReservationTarget"
    ]
    """<p>Information about the target Capacity Reservation or Capacity Reservation group.</p>"""
