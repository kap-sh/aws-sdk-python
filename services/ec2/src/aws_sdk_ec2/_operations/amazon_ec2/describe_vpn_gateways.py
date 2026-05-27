"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnGateways``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_vpn_gateways_request
    import aws_sdk_ec2.types.describe_vpn_gateways_result


def describe_vpn_gateways(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_vpn_gateways_request.DescribeVpnGatewaysRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_vpn_gateways_result.DescribeVpnGatewaysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_vpn_gateways(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_vpn_gateways_request.DescribeVpnGatewaysRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_vpn_gateways_result.DescribeVpnGatewaysResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
