"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_capacity_reservation_request
    import aws_sdk_ec2.types.cancel_capacity_reservation_result


def cancel_capacity_reservation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.cancel_capacity_reservation_request.CancelCapacityReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_capacity_reservation_result.CancelCapacityReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_cancel_capacity_reservation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.cancel_capacity_reservation_request.CancelCapacityReservationRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_capacity_reservation_result.CancelCapacityReservationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
