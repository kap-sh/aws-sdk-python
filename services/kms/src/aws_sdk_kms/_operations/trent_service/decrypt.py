"""Generated from Smithy shape ``com.amazonaws.kms#Decrypt``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.decrypt_request
    import aws_sdk_kms.types.decrypt_response


def decrypt(
    options: OperationOptions, input: aws_sdk_kms.types.decrypt_request.DecryptRequest
) -> tuple[aws_sdk_kms.types.decrypt_response.DecryptResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_decrypt(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.decrypt_request.DecryptRequest,
) -> tuple[aws_sdk_kms.types.decrypt_response.DecryptResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
