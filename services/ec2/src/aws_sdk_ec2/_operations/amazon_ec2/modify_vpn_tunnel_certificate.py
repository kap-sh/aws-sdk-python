"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnTunnelCertificate``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_vpn_tunnel_certificate_request
    import aws_sdk_ec2.types.modify_vpn_tunnel_certificate_result


def modify_vpn_tunnel_certificate(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_vpn_tunnel_certificate_request.ModifyVpnTunnelCertificateRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpn_tunnel_certificate_result.ModifyVpnTunnelCertificateResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_vpn_tunnel_certificate(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_vpn_tunnel_certificate_request.ModifyVpnTunnelCertificateRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpn_tunnel_certificate_result.ModifyVpnTunnelCertificateResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
