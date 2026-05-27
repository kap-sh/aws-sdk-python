"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlocks``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_capacity_blocks_request
    import aws_sdk_ec2.types.describe_capacity_blocks_result


def describe_capacity_blocks(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_capacity_blocks_request.DescribeCapacityBlocksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_capacity_blocks_result.DescribeCapacityBlocksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_capacity_blocks(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_capacity_blocks_request.DescribeCapacityBlocksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_capacity_blocks_result.DescribeCapacityBlocksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
