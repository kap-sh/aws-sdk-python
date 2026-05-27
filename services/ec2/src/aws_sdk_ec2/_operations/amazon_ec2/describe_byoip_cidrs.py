"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeByoipCidrs``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_byoip_cidrs_request
    import aws_sdk_ec2.types.describe_byoip_cidrs_result


def describe_byoip_cidrs(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_byoip_cidrs_request.DescribeByoipCidrsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_byoip_cidrs_result.DescribeByoipCidrsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_byoip_cidrs(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_byoip_cidrs_request.DescribeByoipCidrsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_byoip_cidrs_result.DescribeByoipCidrsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
