"""Generated from Smithy shape ``com.amazonaws.iam#ListVirtualMFADevices``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_virtual_mfa_devices_request
    import aws_sdk_iam.types.list_virtual_mfa_devices_response


def list_virtual_mfa_devices(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_virtual_mfa_devices_request.ListVirtualMFADevicesRequest,
) -> tuple[
    aws_sdk_iam.types.list_virtual_mfa_devices_response.ListVirtualMFADevicesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_virtual_mfa_devices(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_virtual_mfa_devices_request.ListVirtualMFADevicesRequest,
) -> tuple[
    aws_sdk_iam.types.list_virtual_mfa_devices_response.ListVirtualMFADevicesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
