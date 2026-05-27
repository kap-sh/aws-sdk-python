"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHosts``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_hosts_request
    import aws_sdk_ec2.types.describe_hosts_result


def describe_hosts(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_hosts_request.DescribeHostsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_hosts_result.DescribeHostsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_hosts(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_hosts_request.DescribeHostsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_hosts_result.DescribeHostsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
