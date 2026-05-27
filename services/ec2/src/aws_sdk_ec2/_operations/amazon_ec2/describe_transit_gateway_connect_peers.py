"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayConnectPeers``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_transit_gateway_connect_peers_request
    import aws_sdk_ec2.types.describe_transit_gateway_connect_peers_result


def describe_transit_gateway_connect_peers(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_transit_gateway_connect_peers_request.DescribeTransitGatewayConnectPeersRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_transit_gateway_connect_peers_result.DescribeTransitGatewayConnectPeersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_transit_gateway_connect_peers(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_transit_gateway_connect_peers_request.DescribeTransitGatewayConnectPeersRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_transit_gateway_connect_peers_result.DescribeTransitGatewayConnectPeersResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
