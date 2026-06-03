"""Generated from Smithy shape ``com.amazonaws.kms#Encrypt``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.encrypt_request
    import awd_sdk_kms.types.encrypt_response


def encrypt(
    options: OperationOptions, input: awd_sdk_kms.types.encrypt_request.EncryptRequest
) -> tuple[awd_sdk_kms.types.encrypt_response.EncryptResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_encrypt(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.encrypt_request.EncryptRequest,
) -> tuple[awd_sdk_kms.types.encrypt_response.EncryptResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
