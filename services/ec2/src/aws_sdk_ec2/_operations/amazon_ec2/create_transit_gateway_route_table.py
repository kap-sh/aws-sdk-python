"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayRouteTable``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_transit_gateway_route_table_request
    import aws_sdk_ec2.types.create_transit_gateway_route_table_result


def create_transit_gateway_route_table(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_transit_gateway_route_table_request.CreateTransitGatewayRouteTableRequest,
) -> tuple[
    aws_sdk_ec2.types.create_transit_gateway_route_table_result.CreateTransitGatewayRouteTableResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_transit_gateway_route_table(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_transit_gateway_route_table_request.CreateTransitGatewayRouteTableRequest,
) -> tuple[
    aws_sdk_ec2.types.create_transit_gateway_route_table_result.CreateTransitGatewayRouteTableResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
