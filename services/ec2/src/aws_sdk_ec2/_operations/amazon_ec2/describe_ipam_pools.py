"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPools``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_ipam_pools_request
    import aws_sdk_ec2.types.describe_ipam_pools_result


def describe_ipam_pools(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_ipam_pools_request.DescribeIpamPoolsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipam_pools_result.DescribeIpamPoolsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_ipam_pools(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_ipam_pools_request.DescribeIpamPoolsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipam_pools_result.DescribeIpamPoolsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
