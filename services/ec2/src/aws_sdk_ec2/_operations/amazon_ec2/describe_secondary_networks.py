"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondaryNetworks``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_secondary_networks_request
    import aws_sdk_ec2.types.describe_secondary_networks_result


def describe_secondary_networks(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_secondary_networks_request.DescribeSecondaryNetworksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_secondary_networks_result.DescribeSecondaryNetworksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_secondary_networks(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_secondary_networks_request.DescribeSecondaryNetworksRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_secondary_networks_result.DescribeSecondaryNetworksResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
