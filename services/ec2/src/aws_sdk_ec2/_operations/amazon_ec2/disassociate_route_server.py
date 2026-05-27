"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateRouteServer``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_route_server_request
    import aws_sdk_ec2.types.disassociate_route_server_result


def disassociate_route_server(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_route_server_request.DisassociateRouteServerRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_route_server_result.DisassociateRouteServerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_route_server(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_route_server_request.DisassociateRouteServerRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_route_server_result.DisassociateRouteServerResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
