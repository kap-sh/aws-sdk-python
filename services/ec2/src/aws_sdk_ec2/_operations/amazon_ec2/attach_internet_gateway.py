"""Generated from Smithy shape ``com.amazonaws.ec2#AttachInternetGateway``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.attach_internet_gateway_request


def attach_internet_gateway(
    options: OperationOptions,
    input: aws_sdk_ec2.types.attach_internet_gateway_request.AttachInternetGatewayRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_attach_internet_gateway(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.attach_internet_gateway_request.AttachInternetGatewayRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
