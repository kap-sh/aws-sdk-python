"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayRouteTableAnnouncements``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_transit_gateway_route_table_announcements_request
    import aws_sdk_ec2.types.describe_transit_gateway_route_table_announcements_result


def describe_transit_gateway_route_table_announcements(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_transit_gateway_route_table_announcements_request.DescribeTransitGatewayRouteTableAnnouncementsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_transit_gateway_route_table_announcements_result.DescribeTransitGatewayRouteTableAnnouncementsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_transit_gateway_route_table_announcements(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_transit_gateway_route_table_announcements_request.DescribeTransitGatewayRouteTableAnnouncementsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_transit_gateway_route_table_announcements_result.DescribeTransitGatewayRouteTableAnnouncementsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
