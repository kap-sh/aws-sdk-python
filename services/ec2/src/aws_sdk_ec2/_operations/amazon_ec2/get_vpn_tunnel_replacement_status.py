"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnTunnelReplacementStatus``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_vpn_tunnel_replacement_status_request
    import aws_sdk_ec2.types.get_vpn_tunnel_replacement_status_result


def get_vpn_tunnel_replacement_status(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_vpn_tunnel_replacement_status_request.GetVpnTunnelReplacementStatusRequest,
) -> tuple[
    aws_sdk_ec2.types.get_vpn_tunnel_replacement_status_result.GetVpnTunnelReplacementStatusResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_vpn_tunnel_replacement_status(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_vpn_tunnel_replacement_status_request.GetVpnTunnelReplacementStatusRequest,
) -> tuple[
    aws_sdk_ec2.types.get_vpn_tunnel_replacement_status_result.GetVpnTunnelReplacementStatusResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
