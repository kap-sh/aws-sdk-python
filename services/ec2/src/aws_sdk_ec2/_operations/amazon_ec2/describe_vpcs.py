"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcs``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_vpcs_request
    import aws_sdk_ec2.types.describe_vpcs_result


def describe_vpcs(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_vpcs_request.DescribeVpcsRequest,
) -> tuple[aws_sdk_ec2.types.describe_vpcs_result.DescribeVpcsResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_vpcs(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_vpcs_request.DescribeVpcsRequest,
) -> tuple[aws_sdk_ec2.types.describe_vpcs_result.DescribeVpcsResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
