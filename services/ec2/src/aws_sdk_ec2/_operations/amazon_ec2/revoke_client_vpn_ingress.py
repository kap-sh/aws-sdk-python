"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeClientVpnIngress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.revoke_client_vpn_ingress_request
    import aws_sdk_ec2.types.revoke_client_vpn_ingress_result


def revoke_client_vpn_ingress(
    options: OperationOptions,
    input: aws_sdk_ec2.types.revoke_client_vpn_ingress_request.RevokeClientVpnIngressRequest,
) -> tuple[
    aws_sdk_ec2.types.revoke_client_vpn_ingress_result.RevokeClientVpnIngressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_revoke_client_vpn_ingress(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.revoke_client_vpn_ingress_request.RevokeClientVpnIngressRequest,
) -> tuple[
    aws_sdk_ec2.types.revoke_client_vpn_ingress_result.RevokeClientVpnIngressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
