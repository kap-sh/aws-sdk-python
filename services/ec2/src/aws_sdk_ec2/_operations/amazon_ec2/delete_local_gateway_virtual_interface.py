"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayVirtualInterface``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_local_gateway_virtual_interface_request
    import aws_sdk_ec2.types.delete_local_gateway_virtual_interface_result


def delete_local_gateway_virtual_interface(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_local_gateway_virtual_interface_request.DeleteLocalGatewayVirtualInterfaceRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_local_gateway_virtual_interface_result.DeleteLocalGatewayVirtualInterfaceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_local_gateway_virtual_interface(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_local_gateway_virtual_interface_request.DeleteLocalGatewayVirtualInterfaceRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_local_gateway_virtual_interface_result.DeleteLocalGatewayVirtualInterfaceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
