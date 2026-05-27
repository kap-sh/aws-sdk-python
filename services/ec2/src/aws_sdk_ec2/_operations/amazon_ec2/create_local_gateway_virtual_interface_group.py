"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayVirtualInterfaceGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_local_gateway_virtual_interface_group_request
    import aws_sdk_ec2.types.create_local_gateway_virtual_interface_group_result


def create_local_gateway_virtual_interface_group(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_local_gateway_virtual_interface_group_request.CreateLocalGatewayVirtualInterfaceGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.create_local_gateway_virtual_interface_group_result.CreateLocalGatewayVirtualInterfaceGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_local_gateway_virtual_interface_group(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_local_gateway_virtual_interface_group_request.CreateLocalGatewayVirtualInterfaceGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.create_local_gateway_virtual_interface_group_result.CreateLocalGatewayVirtualInterfaceGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
