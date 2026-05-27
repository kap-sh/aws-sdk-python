"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteCustomerGateway``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_customer_gateway_request


def delete_customer_gateway(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_customer_gateway_request.DeleteCustomerGatewayRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_customer_gateway(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_customer_gateway_request.DeleteCustomerGatewayRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
