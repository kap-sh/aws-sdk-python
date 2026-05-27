"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_host_reservations_request
    import aws_sdk_ec2.types.describe_host_reservations_result


def describe_host_reservations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_host_reservations_request.DescribeHostReservationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_host_reservations_result.DescribeHostReservationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_host_reservations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_host_reservations_request.DescribeHostReservationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_host_reservations_result.DescribeHostReservationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
