"""Generated from Smithy shape ``com.amazonaws.kms#UpdateKeyDescription``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.update_key_description_request


def update_key_description(
    options: OperationOptions,
    input: awd_sdk_kms.types.update_key_description_request.UpdateKeyDescriptionRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_key_description(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.update_key_description_request.UpdateKeyDescriptionRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
