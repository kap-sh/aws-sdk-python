"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRoute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_route_request


def delete_route(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_route_request.DeleteRouteRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_route(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_route_request.DeleteRouteRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
