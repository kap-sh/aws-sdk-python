"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_id

ReservedInstancesIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.reservation_id.ReservationId"
]
