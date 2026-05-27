"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockStatus``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_capacity_block_status_request
    import aws_sdk_ec2.types.describe_capacity_block_status_result


def describe_capacity_block_status(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_capacity_block_status_request.DescribeCapacityBlockStatusRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_capacity_block_status_result.DescribeCapacityBlockStatusResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_capacity_block_status(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_capacity_block_status_request.DescribeCapacityBlockStatusRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_capacity_block_status_result.DescribeCapacityBlockStatusResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
