"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnEndpoints``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_client_vpn_endpoints_request
    import aws_sdk_ec2.types.describe_client_vpn_endpoints_result


def describe_client_vpn_endpoints(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_client_vpn_endpoints_request.DescribeClientVpnEndpointsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_client_vpn_endpoints_result.DescribeClientVpnEndpointsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_client_vpn_endpoints(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_client_vpn_endpoints_request.DescribeClientVpnEndpointsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_client_vpn_endpoints_result.DescribeClientVpnEndpointsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
