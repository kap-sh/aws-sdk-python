"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCoipPools``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_coip_pools_request
    import aws_sdk_ec2.types.describe_coip_pools_result


def describe_coip_pools(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_coip_pools_request.DescribeCoipPoolsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_coip_pools_result.DescribeCoipPoolsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_coip_pools(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_coip_pools_request.DescribeCoipPoolsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_coip_pools_result.DescribeCoipPoolsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
