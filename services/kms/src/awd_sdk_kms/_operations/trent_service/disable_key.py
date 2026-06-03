"""Generated from Smithy shape ``com.amazonaws.kms#DisableKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.disable_key_request


def disable_key(
    options: OperationOptions,
    input: awd_sdk_kms.types.disable_key_request.DisableKeyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_key(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.disable_key_request.DisableKeyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
