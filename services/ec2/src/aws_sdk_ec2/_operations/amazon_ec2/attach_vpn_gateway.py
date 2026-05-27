"""Generated from Smithy shape ``com.amazonaws.ec2#AttachVpnGateway``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attach_vpn_gateway_request
    import aws_sdk_ec2.types.attach_vpn_gateway_result


def attach_vpn_gateway(
    options: OperationOptions,
    input: aws_sdk_ec2.types.attach_vpn_gateway_request.AttachVpnGatewayRequest,
) -> tuple[
    aws_sdk_ec2.types.attach_vpn_gateway_result.AttachVpnGatewayResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_attach_vpn_gateway(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.attach_vpn_gateway_request.AttachVpnGatewayRequest,
) -> tuple[
    aws_sdk_ec2.types.attach_vpn_gateway_result.AttachVpnGatewayResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
