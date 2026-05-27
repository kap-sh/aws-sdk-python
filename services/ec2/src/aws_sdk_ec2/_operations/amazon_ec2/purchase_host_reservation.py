"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseHostReservation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.purchase_host_reservation_request
    import aws_sdk_ec2.types.purchase_host_reservation_result


def purchase_host_reservation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.purchase_host_reservation_request.PurchaseHostReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.purchase_host_reservation_result.PurchaseHostReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_purchase_host_reservation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.purchase_host_reservation_request.PurchaseHostReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.purchase_host_reservation_result.PurchaseHostReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
