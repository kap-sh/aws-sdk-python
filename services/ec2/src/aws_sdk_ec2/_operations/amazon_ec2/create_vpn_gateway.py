"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnGateway``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_vpn_gateway_request
    import aws_sdk_ec2.types.create_vpn_gateway_result


def create_vpn_gateway(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_vpn_gateway_request.CreateVpnGatewayRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpn_gateway_result.CreateVpnGatewayResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_vpn_gateway(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_vpn_gateway_request.CreateVpnGatewayRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpn_gateway_result.CreateVpnGatewayResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
