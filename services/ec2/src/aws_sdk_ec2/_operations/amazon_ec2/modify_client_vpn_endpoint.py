"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyClientVpnEndpoint``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_client_vpn_endpoint_request
    import aws_sdk_ec2.types.modify_client_vpn_endpoint_result


def modify_client_vpn_endpoint(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_client_vpn_endpoint_request.ModifyClientVpnEndpointRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_client_vpn_endpoint_result.ModifyClientVpnEndpointResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_client_vpn_endpoint(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_client_vpn_endpoint_request.ModifyClientVpnEndpointRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_client_vpn_endpoint_result.ModifyClientVpnEndpointResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
