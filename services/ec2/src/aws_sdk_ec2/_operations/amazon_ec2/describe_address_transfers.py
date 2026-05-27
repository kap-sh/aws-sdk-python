"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAddressTransfers``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_address_transfers_request
    import aws_sdk_ec2.types.describe_address_transfers_result


def describe_address_transfers(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_address_transfers_request.DescribeAddressTransfersRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_address_transfers_result.DescribeAddressTransfersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_address_transfers(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_address_transfers_request.DescribeAddressTransfersRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_address_transfers_result.DescribeAddressTransfersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
