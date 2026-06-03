"""Generated from Smithy shape ``com.amazonaws.kms#DisconnectCustomKeyStore``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.disconnect_custom_key_store_request
    import aws_sdk_kms.types.disconnect_custom_key_store_response


def disconnect_custom_key_store(
    options: OperationOptions,
    input: aws_sdk_kms.types.disconnect_custom_key_store_request.DisconnectCustomKeyStoreRequest,
) -> tuple[
    aws_sdk_kms.types.disconnect_custom_key_store_response.DisconnectCustomKeyStoreResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disconnect_custom_key_store(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.disconnect_custom_key_store_request.DisconnectCustomKeyStoreRequest,
) -> tuple[
    aws_sdk_kms.types.disconnect_custom_key_store_response.DisconnectCustomKeyStoreResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
