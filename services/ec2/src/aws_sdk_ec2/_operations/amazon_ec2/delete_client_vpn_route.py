"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteClientVpnRoute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_client_vpn_route_request
    import aws_sdk_ec2.types.delete_client_vpn_route_result


def delete_client_vpn_route(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_client_vpn_route_request.DeleteClientVpnRouteRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_client_vpn_route_result.DeleteClientVpnRouteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_client_vpn_route(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_client_vpn_route_request.DeleteClientVpnRouteRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_client_vpn_route_result.DeleteClientVpnRouteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
