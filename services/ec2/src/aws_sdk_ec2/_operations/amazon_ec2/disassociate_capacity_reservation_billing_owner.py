"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateCapacityReservationBillingOwner``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_capacity_reservation_billing_owner_request
    import aws_sdk_ec2.types.disassociate_capacity_reservation_billing_owner_result


def disassociate_capacity_reservation_billing_owner(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_capacity_reservation_billing_owner_request.DisassociateCapacityReservationBillingOwnerRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_capacity_reservation_billing_owner_result.DisassociateCapacityReservationBillingOwnerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_capacity_reservation_billing_owner(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_capacity_reservation_billing_owner_request.DisassociateCapacityReservationBillingOwnerRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_capacity_reservation_billing_owner_result.DisassociateCapacityReservationBillingOwnerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
