"""Generated from Smithy shape ``com.amazonaws.kms#DeleteCustomKeyStore``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.delete_custom_key_store_request
    import awd_sdk_kms.types.delete_custom_key_store_response


def delete_custom_key_store(
    options: OperationOptions,
    input: awd_sdk_kms.types.delete_custom_key_store_request.DeleteCustomKeyStoreRequest,
) -> tuple[
    awd_sdk_kms.types.delete_custom_key_store_response.DeleteCustomKeyStoreResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_custom_key_store(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.delete_custom_key_store_request.DeleteCustomKeyStoreRequest,
) -> tuple[
    awd_sdk_kms.types.delete_custom_key_store_response.DeleteCustomKeyStoreResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
