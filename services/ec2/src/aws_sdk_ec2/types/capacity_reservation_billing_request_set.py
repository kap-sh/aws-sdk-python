"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationBillingRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_billing_request

CapacityReservationBillingRequestSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_billing_request.CapacityReservationBillingRequest"
]
