"""Generated from Smithy shape ``com.amazonaws.ec2#HostReservationIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host_reservation_id

HostReservationIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.host_reservation_id.HostReservationId"
]
