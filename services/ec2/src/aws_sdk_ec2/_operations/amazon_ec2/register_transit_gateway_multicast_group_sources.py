"""Generated from Smithy shape ``com.amazonaws.ec2#RegisterTransitGatewayMulticastGroupSources``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.register_transit_gateway_multicast_group_sources_request
    import aws_sdk_ec2.types.register_transit_gateway_multicast_group_sources_result


def register_transit_gateway_multicast_group_sources(
    options: OperationOptions,
    input: aws_sdk_ec2.types.register_transit_gateway_multicast_group_sources_request.RegisterTransitGatewayMulticastGroupSourcesRequest,
) -> tuple[
    aws_sdk_ec2.types.register_transit_gateway_multicast_group_sources_result.RegisterTransitGatewayMulticastGroupSourcesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_register_transit_gateway_multicast_group_sources(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.register_transit_gateway_multicast_group_sources_request.RegisterTransitGatewayMulticastGroupSourcesRequest,
) -> tuple[
    aws_sdk_ec2.types.register_transit_gateway_multicast_group_sources_result.RegisterTransitGatewayMulticastGroupSourcesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
