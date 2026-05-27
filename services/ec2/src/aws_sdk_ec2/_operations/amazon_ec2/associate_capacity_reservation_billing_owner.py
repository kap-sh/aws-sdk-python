"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateCapacityReservationBillingOwner``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_request
    import aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_result


def associate_capacity_reservation_billing_owner(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_request.AssociateCapacityReservationBillingOwnerRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_result.AssociateCapacityReservationBillingOwnerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_capacity_reservation_billing_owner(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_request.AssociateCapacityReservationBillingOwnerRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_capacity_reservation_billing_owner_result.AssociateCapacityReservationBillingOwnerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
