"""Generated from Smithy shape ``com.amazonaws.kms#ListKeys``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.list_keys_request
    import awd_sdk_kms.types.list_keys_response


def list_keys(
    options: OperationOptions,
    input: awd_sdk_kms.types.list_keys_request.ListKeysRequest,
) -> tuple[awd_sdk_kms.types.list_keys_response.ListKeysResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_keys(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.list_keys_request.ListKeysRequest,
) -> tuple[awd_sdk_kms.types.list_keys_response.ListKeysResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
