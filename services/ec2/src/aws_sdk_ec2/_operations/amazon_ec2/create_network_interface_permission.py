"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfacePermission``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_network_interface_permission_request
    import aws_sdk_ec2.types.create_network_interface_permission_result


def create_network_interface_permission(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_network_interface_permission_request.CreateNetworkInterfacePermissionRequest,
) -> tuple[
    aws_sdk_ec2.types.create_network_interface_permission_result.CreateNetworkInterfacePermissionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_network_interface_permission(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_network_interface_permission_request.CreateNetworkInterfacePermissionRequest,
) -> tuple[
    aws_sdk_ec2.types.create_network_interface_permission_result.CreateNetworkInterfacePermissionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
