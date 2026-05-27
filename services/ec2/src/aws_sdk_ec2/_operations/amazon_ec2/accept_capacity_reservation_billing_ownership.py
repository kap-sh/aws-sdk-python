"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptCapacityReservationBillingOwnership``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_request
    import aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_result


def accept_capacity_reservation_billing_ownership(
    options: OperationOptions,
    input: aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_request.AcceptCapacityReservationBillingOwnershipRequest,
) -> tuple[
    aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_result.AcceptCapacityReservationBillingOwnershipResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_accept_capacity_reservation_billing_ownership(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_request.AcceptCapacityReservationBillingOwnershipRequest,
) -> tuple[
    aws_sdk_ec2.types.accept_capacity_reservation_billing_ownership_result.AcceptCapacityReservationBillingOwnershipResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
