"""Generated from Smithy shape ``com.amazonaws.kms#GetPublicKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.get_public_key_request
    import aws_sdk_kms.types.get_public_key_response


def get_public_key(
    options: OperationOptions,
    input: aws_sdk_kms.types.get_public_key_request.GetPublicKeyRequest,
) -> tuple[
    aws_sdk_kms.types.get_public_key_response.GetPublicKeyResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_public_key(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.get_public_key_request.GetPublicKeyRequest,
) -> tuple[
    aws_sdk_kms.types.get_public_key_response.GetPublicKeyResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
