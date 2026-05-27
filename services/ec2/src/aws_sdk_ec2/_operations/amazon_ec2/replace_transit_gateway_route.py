"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceTransitGatewayRoute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_transit_gateway_route_request
    import aws_sdk_ec2.types.replace_transit_gateway_route_result


def replace_transit_gateway_route(
    options: OperationOptions,
    input: aws_sdk_ec2.types.replace_transit_gateway_route_request.ReplaceTransitGatewayRouteRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_transit_gateway_route_result.ReplaceTransitGatewayRouteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_replace_transit_gateway_route(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.replace_transit_gateway_route_request.ReplaceTransitGatewayRouteRequest,
) -> tuple[
    aws_sdk_ec2.types.replace_transit_gateway_route_result.ReplaceTransitGatewayRouteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
