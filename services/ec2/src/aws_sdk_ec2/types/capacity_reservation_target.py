"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.string


class CapacityReservationTarget(TypedDict):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation in which to run the instance.</p>"""
    capacity_reservation_resource_group_arn: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p>The ARN of the Capacity Reservation resource group in which to run the instance.</p>"""
