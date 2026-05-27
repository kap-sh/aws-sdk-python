"""Generated from Smithy shape ``com.amazonaws.ec2#DisableTransitGatewayRouteTablePropagation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_transit_gateway_route_table_propagation_request
    import aws_sdk_ec2.types.disable_transit_gateway_route_table_propagation_result


def disable_transit_gateway_route_table_propagation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_transit_gateway_route_table_propagation_request.DisableTransitGatewayRouteTablePropagationRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_transit_gateway_route_table_propagation_result.DisableTransitGatewayRouteTablePropagationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_transit_gateway_route_table_propagation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_transit_gateway_route_table_propagation_request.DisableTransitGatewayRouteTablePropagationRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_transit_gateway_route_table_propagation_result.DisableTransitGatewayRouteTablePropagationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
