"""Generated from Smithy shape ``com.amazonaws.iam#UntagMFADevice``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.untag_mfa_device_request


def untag_mfa_device(
    options: OperationOptions,
    input: aws_sdk_iam.types.untag_mfa_device_request.UntagMFADeviceRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_untag_mfa_device(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.untag_mfa_device_request.UntagMFADeviceRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
