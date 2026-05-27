"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceConnectEndpoints``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_instance_connect_endpoints_request
    import aws_sdk_ec2.types.describe_instance_connect_endpoints_result


def describe_instance_connect_endpoints(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_instance_connect_endpoints_request.DescribeInstanceConnectEndpointsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_instance_connect_endpoints_result.DescribeInstanceConnectEndpointsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_instance_connect_endpoints(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_instance_connect_endpoints_request.DescribeInstanceConnectEndpointsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_instance_connect_endpoints_result.DescribeInstanceConnectEndpointsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
