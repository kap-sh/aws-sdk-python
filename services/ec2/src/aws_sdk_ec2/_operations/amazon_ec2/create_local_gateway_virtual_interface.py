"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayVirtualInterface``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_local_gateway_virtual_interface_request
    import aws_sdk_ec2.types.create_local_gateway_virtual_interface_result


def create_local_gateway_virtual_interface(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_local_gateway_virtual_interface_request.CreateLocalGatewayVirtualInterfaceRequest,
) -> tuple[
    aws_sdk_ec2.types.create_local_gateway_virtual_interface_result.CreateLocalGatewayVirtualInterfaceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_local_gateway_virtual_interface(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_local_gateway_virtual_interface_request.CreateLocalGatewayVirtualInterfaceRequest,
) -> tuple[
    aws_sdk_ec2.types.create_local_gateway_virtual_interface_result.CreateLocalGatewayVirtualInterfaceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
