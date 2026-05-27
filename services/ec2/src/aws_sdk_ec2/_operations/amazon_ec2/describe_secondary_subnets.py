"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondarySubnets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_secondary_subnets_request
    import aws_sdk_ec2.types.describe_secondary_subnets_result


def describe_secondary_subnets(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_secondary_subnets_request.DescribeSecondarySubnetsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_secondary_subnets_result.DescribeSecondarySubnetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_secondary_subnets(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_secondary_subnets_request.DescribeSecondarySubnetsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_secondary_subnets_result.DescribeSecondarySubnetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
