"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservationFleets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_capacity_reservation_fleets_request
    import aws_sdk_ec2.types.cancel_capacity_reservation_fleets_result


def cancel_capacity_reservation_fleets(
    options: OperationOptions,
    input: aws_sdk_ec2.types.cancel_capacity_reservation_fleets_request.CancelCapacityReservationFleetsRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_capacity_reservation_fleets_result.CancelCapacityReservationFleetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_cancel_capacity_reservation_fleets(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.cancel_capacity_reservation_fleets_request.CancelCapacityReservationFleetsRequest,
) -> tuple[
    aws_sdk_ec2.types.cancel_capacity_reservation_fleets_result.CancelCapacityReservationFleetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
