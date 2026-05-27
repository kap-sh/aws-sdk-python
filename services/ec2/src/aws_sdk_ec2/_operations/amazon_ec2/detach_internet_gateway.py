"""Generated from Smithy shape ``com.amazonaws.ec2#DetachInternetGateway``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.detach_internet_gateway_request


def detach_internet_gateway(
    options: OperationOptions,
    input: aws_sdk_ec2.types.detach_internet_gateway_request.DetachInternetGatewayRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_detach_internet_gateway(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.detach_internet_gateway_request.DetachInternetGatewayRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
