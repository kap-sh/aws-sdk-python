"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_id

ReservedInstanceIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.reservation_id.ReservationId"
]
