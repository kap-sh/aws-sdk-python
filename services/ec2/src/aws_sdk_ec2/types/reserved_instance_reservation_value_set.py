"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceReservationValueSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instance_reservation_value

ReservedInstanceReservationValueSet: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instance_reservation_value.ReservedInstanceReservationValue"
]
