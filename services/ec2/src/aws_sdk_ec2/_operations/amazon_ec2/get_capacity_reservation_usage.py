"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityReservationUsage``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_capacity_reservation_usage_request
    import aws_sdk_ec2.types.get_capacity_reservation_usage_result


def get_capacity_reservation_usage(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_capacity_reservation_usage_request.GetCapacityReservationUsageRequest,
) -> tuple[
    aws_sdk_ec2.types.get_capacity_reservation_usage_result.GetCapacityReservationUsageResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_capacity_reservation_usage(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_capacity_reservation_usage_request.GetCapacityReservationUsageRequest,
) -> tuple[
    aws_sdk_ec2.types.get_capacity_reservation_usage_result.GetCapacityReservationUsageResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
