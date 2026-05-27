"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPrefixListResolvers``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_ipam_prefix_list_resolvers_request
    import aws_sdk_ec2.types.describe_ipam_prefix_list_resolvers_result


def describe_ipam_prefix_list_resolvers(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_ipam_prefix_list_resolvers_request.DescribeIpamPrefixListResolversRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipam_prefix_list_resolvers_result.DescribeIpamPrefixListResolversResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_ipam_prefix_list_resolvers(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_ipam_prefix_list_resolvers_request.DescribeIpamPrefixListResolversRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipam_prefix_list_resolvers_result.DescribeIpamPrefixListResolversResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
