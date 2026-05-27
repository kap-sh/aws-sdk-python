"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteServer``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_route_server_request
    import aws_sdk_ec2.types.delete_route_server_result


def delete_route_server(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_route_server_request.DeleteRouteServerRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_route_server_result.DeleteRouteServerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_route_server(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_route_server_request.DeleteRouteServerRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_route_server_result.DeleteRouteServerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
