"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeClientVpnIngress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.authorize_client_vpn_ingress_request
    import aws_sdk_ec2.types.authorize_client_vpn_ingress_result


def authorize_client_vpn_ingress(
    options: OperationOptions,
    input: aws_sdk_ec2.types.authorize_client_vpn_ingress_request.AuthorizeClientVpnIngressRequest,
) -> tuple[
    aws_sdk_ec2.types.authorize_client_vpn_ingress_result.AuthorizeClientVpnIngressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_authorize_client_vpn_ingress(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.authorize_client_vpn_ingress_request.AuthorizeClientVpnIngressRequest,
) -> tuple[
    aws_sdk_ec2.types.authorize_client_vpn_ingress_result.AuthorizeClientVpnIngressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
