"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationFleetInstanceSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_fleet_instance_specification

ReservationFleetInstanceSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.reservation_fleet_instance_specification.ReservationFleetInstanceSpecification"
]
