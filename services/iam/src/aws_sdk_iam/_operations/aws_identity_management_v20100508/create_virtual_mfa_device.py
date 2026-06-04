"""Generated from Smithy shape ``com.amazonaws.iam#CreateVirtualMFADevice``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_virtual_mfa_device_request
    import aws_sdk_iam.types.create_virtual_mfa_device_response


def create_virtual_mfa_device(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_virtual_mfa_device_request.CreateVirtualMFADeviceRequest,
) -> tuple[
    aws_sdk_iam.types.create_virtual_mfa_device_response.CreateVirtualMFADeviceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_virtual_mfa_device(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_virtual_mfa_device_request.CreateVirtualMFADeviceRequest,
) -> tuple[
    aws_sdk_iam.types.create_virtual_mfa_device_response.CreateVirtualMFADeviceResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
