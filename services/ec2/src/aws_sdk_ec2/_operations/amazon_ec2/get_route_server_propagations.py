"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerPropagations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_route_server_propagations_request
    import aws_sdk_ec2.types.get_route_server_propagations_result


def get_route_server_propagations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_route_server_propagations_request.GetRouteServerPropagationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_route_server_propagations_result.GetRouteServerPropagationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_route_server_propagations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_route_server_propagations_request.GetRouteServerPropagationsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_route_server_propagations_result.GetRouteServerPropagationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
