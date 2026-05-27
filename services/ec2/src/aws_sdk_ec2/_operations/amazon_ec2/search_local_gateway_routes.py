"""Generated from Smithy shape ``com.amazonaws.ec2#SearchLocalGatewayRoutes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.search_local_gateway_routes_request
    import aws_sdk_ec2.types.search_local_gateway_routes_result


def search_local_gateway_routes(
    options: OperationOptions,
    input: aws_sdk_ec2.types.search_local_gateway_routes_request.SearchLocalGatewayRoutesRequest,
) -> tuple[
    aws_sdk_ec2.types.search_local_gateway_routes_result.SearchLocalGatewayRoutesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_search_local_gateway_routes(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.search_local_gateway_routes_request.SearchLocalGatewayRoutesRequest,
) -> tuple[
    aws_sdk_ec2.types.search_local_gateway_routes_result.SearchLocalGatewayRoutesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
