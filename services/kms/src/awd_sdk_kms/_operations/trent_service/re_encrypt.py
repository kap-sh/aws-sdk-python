"""Generated from Smithy shape ``com.amazonaws.kms#ReEncrypt``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.re_encrypt_request
    import awd_sdk_kms.types.re_encrypt_response


def re_encrypt(
    options: OperationOptions,
    input: awd_sdk_kms.types.re_encrypt_request.ReEncryptRequest,
) -> tuple[awd_sdk_kms.types.re_encrypt_response.ReEncryptResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_re_encrypt(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.re_encrypt_request.ReEncryptRequest,
) -> tuple[awd_sdk_kms.types.re_encrypt_response.ReEncryptResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
