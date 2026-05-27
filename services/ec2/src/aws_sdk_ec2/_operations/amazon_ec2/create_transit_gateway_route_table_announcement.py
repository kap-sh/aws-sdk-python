"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayRouteTableAnnouncement``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_transit_gateway_route_table_announcement_request
    import aws_sdk_ec2.types.create_transit_gateway_route_table_announcement_result


def create_transit_gateway_route_table_announcement(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_transit_gateway_route_table_announcement_request.CreateTransitGatewayRouteTableAnnouncementRequest,
) -> tuple[
    aws_sdk_ec2.types.create_transit_gateway_route_table_announcement_result.CreateTransitGatewayRouteTableAnnouncementResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_transit_gateway_route_table_announcement(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_transit_gateway_route_table_announcement_request.CreateTransitGatewayRouteTableAnnouncementRequest,
) -> tuple[
    aws_sdk_ec2.types.create_transit_gateway_route_table_announcement_result.CreateTransitGatewayRouteTableAnnouncementResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
