"""Generated from Smithy shape ``com.amazonaws.kms#EnableKeyRotation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.enable_key_rotation_request


def enable_key_rotation(
    options: OperationOptions,
    input: awd_sdk_kms.types.enable_key_rotation_request.EnableKeyRotationRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_key_rotation(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.enable_key_rotation_request.EnableKeyRotationRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
