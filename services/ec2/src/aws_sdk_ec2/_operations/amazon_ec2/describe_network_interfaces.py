"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInterfaces``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_network_interfaces_request
    import aws_sdk_ec2.types.describe_network_interfaces_result


def describe_network_interfaces(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_network_interfaces_request.DescribeNetworkInterfacesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_network_interfaces_result.DescribeNetworkInterfacesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_network_interfaces(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_network_interfaces_request.DescribeNetworkInterfacesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_network_interfaces_result.DescribeNetworkInterfacesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
