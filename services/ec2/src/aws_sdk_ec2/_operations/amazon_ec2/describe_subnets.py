"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSubnets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_subnets_request
    import aws_sdk_ec2.types.describe_subnets_result


def describe_subnets(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_subnets_request.DescribeSubnetsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_subnets_result.DescribeSubnetsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_subnets(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_subnets_request.DescribeSubnetsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_subnets_result.DescribeSubnetsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
