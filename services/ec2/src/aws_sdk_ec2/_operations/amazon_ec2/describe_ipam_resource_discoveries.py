"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamResourceDiscoveries``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_ipam_resource_discoveries_request
    import aws_sdk_ec2.types.describe_ipam_resource_discoveries_result


def describe_ipam_resource_discoveries(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_ipam_resource_discoveries_request.DescribeIpamResourceDiscoveriesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipam_resource_discoveries_result.DescribeIpamResourceDiscoveriesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_ipam_resource_discoveries(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_ipam_resource_discoveries_request.DescribeIpamResourceDiscoveriesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipam_resource_discoveries_result.DescribeIpamResourceDiscoveriesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
