"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.capacity_reservation_tenancy
    import aws_sdk_ec2.types.string


class CapacityReservationInfo(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type for the Capacity Reservation.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone for the Capacity Reservation.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>The tenancy of the Capacity Reservation.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone.</p>"""
