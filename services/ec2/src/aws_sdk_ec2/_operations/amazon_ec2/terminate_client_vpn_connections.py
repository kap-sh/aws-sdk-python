"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateClientVpnConnections``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.terminate_client_vpn_connections_request
    import aws_sdk_ec2.types.terminate_client_vpn_connections_result


def terminate_client_vpn_connections(
    options: OperationOptions,
    input: aws_sdk_ec2.types.terminate_client_vpn_connections_request.TerminateClientVpnConnectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.terminate_client_vpn_connections_result.TerminateClientVpnConnectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_terminate_client_vpn_connections(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.terminate_client_vpn_connections_request.TerminateClientVpnConnectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.terminate_client_vpn_connections_result.TerminateClientVpnConnectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
