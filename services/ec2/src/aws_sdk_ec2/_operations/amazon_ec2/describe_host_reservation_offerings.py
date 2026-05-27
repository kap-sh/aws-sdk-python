"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservationOfferings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_host_reservation_offerings_request
    import aws_sdk_ec2.types.describe_host_reservation_offerings_result


def describe_host_reservation_offerings(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_host_reservation_offerings_request.DescribeHostReservationOfferingsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_host_reservation_offerings_result.DescribeHostReservationOfferingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_host_reservation_offerings(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_host_reservation_offerings_request.DescribeHostReservationOfferingsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_host_reservation_offerings_result.DescribeHostReservationOfferingsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
