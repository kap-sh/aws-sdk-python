"""Generated from Smithy shape ``com.amazonaws.ec2#CreateClientVpnRoute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_client_vpn_route_request
    import aws_sdk_ec2.types.create_client_vpn_route_result


def create_client_vpn_route(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_client_vpn_route_request.CreateClientVpnRouteRequest,
) -> tuple[
    aws_sdk_ec2.types.create_client_vpn_route_result.CreateClientVpnRouteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_client_vpn_route(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_client_vpn_route_request.CreateClientVpnRouteRequest,
) -> tuple[
    aws_sdk_ec2.types.create_client_vpn_route_result.CreateClientVpnRouteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
