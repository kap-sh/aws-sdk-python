"""Generated from Smithy shape ``com.amazonaws.ec2#TargetReservationValueSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.target_reservation_value

TargetReservationValueSet: TypeAlias = list[
    "aws_sdk_ec2.types.target_reservation_value.TargetReservationValue"
]
