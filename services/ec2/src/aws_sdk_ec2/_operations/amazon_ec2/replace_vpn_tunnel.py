"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceVpnTunnel``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_vpn_tunnel_request
    import aws_sdk_ec2.types.replace_vpn_tunnel_result


def replace_vpn_tunnel(
    options: OperationOptions,
    input: aws_sdk_ec2.types.replace_vpn_tunnel_request.ReplaceVpnTunnelRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_vpn_tunnel_result.ReplaceVpnTunnelResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_replace_vpn_tunnel(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.replace_vpn_tunnel_request.ReplaceVpnTunnelRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_vpn_tunnel_result.ReplaceVpnTunnelResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
