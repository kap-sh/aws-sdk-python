"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationTargetResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CapacityReservationTargetResponse(TypedDict):
    capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the targeted Capacity Reservation.</p>"""
    capacity_reservation_resource_group_arn: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p>The ARN of the targeted Capacity Reservation group.</p>"""
