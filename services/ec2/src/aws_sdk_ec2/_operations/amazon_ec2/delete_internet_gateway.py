"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInternetGateway``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_internet_gateway_request


def delete_internet_gateway(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_internet_gateway_request.DeleteInternetGatewayRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_internet_gateway(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_internet_gateway_request.DeleteInternetGatewayRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
