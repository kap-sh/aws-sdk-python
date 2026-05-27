"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServerPeers``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_route_server_peers_request
    import aws_sdk_ec2.types.describe_route_server_peers_result


def describe_route_server_peers(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_route_server_peers_request.DescribeRouteServerPeersRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_route_server_peers_result.DescribeRouteServerPeersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_route_server_peers(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_route_server_peers_request.DescribeRouteServerPeersRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_route_server_peers_result.DescribeRouteServerPeersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
