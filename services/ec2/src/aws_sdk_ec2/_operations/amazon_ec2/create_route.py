"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRoute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_route_request
    import aws_sdk_ec2.types.create_route_result


def create_route(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_route_request.CreateRouteRequest,
) -> tuple[aws_sdk_ec2.types.create_route_result.CreateRouteResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_route(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_route_request.CreateRouteRequest,
) -> tuple[aws_sdk_ec2.types.create_route_result.CreateRouteResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
