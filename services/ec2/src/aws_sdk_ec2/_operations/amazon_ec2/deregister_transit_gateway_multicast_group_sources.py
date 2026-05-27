"""Generated from Smithy shape ``com.amazonaws.ec2#DeregisterTransitGatewayMulticastGroupSources``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_sources_request
    import aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_sources_result


def deregister_transit_gateway_multicast_group_sources(
    options: OperationOptions,
    input: aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_sources_request.DeregisterTransitGatewayMulticastGroupSourcesRequest,
) -> tuple[
    aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_sources_result.DeregisterTransitGatewayMulticastGroupSourcesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_deregister_transit_gateway_multicast_group_sources(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_sources_request.DeregisterTransitGatewayMulticastGroupSourcesRequest,
) -> tuple[
    aws_sdk_ec2.types.deregister_transit_gateway_multicast_group_sources_result.DeregisterTransitGatewayMulticastGroupSourcesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
