"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpams``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_ipams_request
    import aws_sdk_ec2.types.describe_ipams_result


def describe_ipams(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_ipams_request.DescribeIpamsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipams_result.DescribeIpamsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_ipams(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_ipams_request.DescribeIpamsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipams_result.DescribeIpamsResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
