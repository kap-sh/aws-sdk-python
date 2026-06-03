"""Generated from Smithy shape ``com.amazonaws.kms#EnableKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.enable_key_request


def enable_key(
    options: OperationOptions,
    input: aws_sdk_kms.types.enable_key_request.EnableKeyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_key(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.enable_key_request.EnableKeyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
