"""Generated from Smithy shape ``com.amazonaws.kms#CreateKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.create_key_request
    import aws_sdk_kms.types.create_key_response


def create_key(
    options: OperationOptions,
    input: aws_sdk_kms.types.create_key_request.CreateKeyRequest,
) -> tuple[aws_sdk_kms.types.create_key_response.CreateKeyResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_key(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.create_key_request.CreateKeyRequest,
) -> tuple[aws_sdk_kms.types.create_key_response.CreateKeyResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
