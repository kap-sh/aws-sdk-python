"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcEndpointConnections``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.accept_vpc_endpoint_connections_request
    import aws_sdk_ec2.types.accept_vpc_endpoint_connections_result


def accept_vpc_endpoint_connections(
    options: OperationOptions,
    input: aws_sdk_ec2.types.accept_vpc_endpoint_connections_request.AcceptVpcEndpointConnectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.accept_vpc_endpoint_connections_result.AcceptVpcEndpointConnectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_accept_vpc_endpoint_connections(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.accept_vpc_endpoint_connections_request.AcceptVpcEndpointConnectionsRequest,
) -> tuple[
    aws_sdk_ec2.types.accept_vpc_endpoint_connections_result.AcceptVpcEndpointConnectionsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
