"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePublicIpv4Pools``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_public_ipv4_pools_request
    import aws_sdk_ec2.types.describe_public_ipv4_pools_result


def describe_public_ipv4_pools(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_public_ipv4_pools_request.DescribePublicIpv4PoolsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_public_ipv4_pools_result.DescribePublicIpv4PoolsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_public_ipv4_pools(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_public_ipv4_pools_request.DescribePublicIpv4PoolsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_public_ipv4_pools_result.DescribePublicIpv4PoolsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
