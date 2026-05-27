"""Generated from Smithy shape ``com.amazonaws.ec2#DisableVgwRoutePropagation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_vgw_route_propagation_request


def disable_vgw_route_propagation(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_vgw_route_propagation_request.DisableVgwRoutePropagationRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_vgw_route_propagation(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_vgw_route_propagation_request.DisableVgwRoutePropagationRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
