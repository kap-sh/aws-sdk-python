"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyRouteServer``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_route_server_request
    import aws_sdk_ec2.types.modify_route_server_result


def modify_route_server(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_route_server_request.ModifyRouteServerRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_route_server_result.ModifyRouteServerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_route_server(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_route_server_request.ModifyRouteServerRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_route_server_result.ModifyRouteServerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
