"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTransitGatewayRoutes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_transit_gateway_routes_request
    import aws_sdk_ec2.types.export_transit_gateway_routes_result


def export_transit_gateway_routes(
    options: OperationOptions,
    input: aws_sdk_ec2.types.export_transit_gateway_routes_request.ExportTransitGatewayRoutesRequest,
) -> tuple[
    aws_sdk_ec2.types.export_transit_gateway_routes_result.ExportTransitGatewayRoutesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_export_transit_gateway_routes(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.export_transit_gateway_routes_request.ExportTransitGatewayRoutesRequest,
) -> tuple[
    aws_sdk_ec2.types.export_transit_gateway_routes_result.ExportTransitGatewayRoutesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
