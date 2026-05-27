"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMovingAddresses``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_moving_addresses_request
    import aws_sdk_ec2.types.describe_moving_addresses_result


def describe_moving_addresses(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_moving_addresses_request.DescribeMovingAddressesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_moving_addresses_result.DescribeMovingAddressesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_moving_addresses(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_moving_addresses_request.DescribeMovingAddressesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_moving_addresses_result.DescribeMovingAddressesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
