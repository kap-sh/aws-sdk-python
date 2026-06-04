"""Generated from Smithy shape ``com.amazonaws.iam#ResyncMFADevice``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.resync_mfa_device_request


def resync_mfa_device(
    options: OperationOptions,
    input: aws_sdk_iam.types.resync_mfa_device_request.ResyncMFADeviceRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_resync_mfa_device(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.resync_mfa_device_request.ResyncMFADeviceRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
