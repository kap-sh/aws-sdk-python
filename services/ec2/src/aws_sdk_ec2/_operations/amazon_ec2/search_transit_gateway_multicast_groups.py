"""Generated from Smithy shape ``com.amazonaws.ec2#SearchTransitGatewayMulticastGroups``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.search_transit_gateway_multicast_groups_request
    import aws_sdk_ec2.types.search_transit_gateway_multicast_groups_result


def search_transit_gateway_multicast_groups(
    options: OperationOptions,
    input: aws_sdk_ec2.types.search_transit_gateway_multicast_groups_request.SearchTransitGatewayMulticastGroupsRequest,
) -> tuple[
    aws_sdk_ec2.types.search_transit_gateway_multicast_groups_result.SearchTransitGatewayMulticastGroupsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_search_transit_gateway_multicast_groups(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.search_transit_gateway_multicast_groups_request.SearchTransitGatewayMulticastGroupsRequest,
) -> tuple[
    aws_sdk_ec2.types.search_transit_gateway_multicast_groups_result.SearchTransitGatewayMulticastGroupsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
