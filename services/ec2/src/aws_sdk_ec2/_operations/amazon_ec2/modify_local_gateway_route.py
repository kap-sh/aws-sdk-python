"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyLocalGatewayRoute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_local_gateway_route_request
    import aws_sdk_ec2.types.modify_local_gateway_route_result


def modify_local_gateway_route(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_local_gateway_route_request.ModifyLocalGatewayRouteRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_local_gateway_route_result.ModifyLocalGatewayRouteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_local_gateway_route(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_local_gateway_route_request.ModifyLocalGatewayRouteRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_local_gateway_route_result.ModifyLocalGatewayRouteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
