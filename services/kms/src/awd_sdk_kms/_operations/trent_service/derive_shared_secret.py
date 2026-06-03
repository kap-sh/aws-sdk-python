"""Generated from Smithy shape ``com.amazonaws.kms#DeriveSharedSecret``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.derive_shared_secret_request
    import awd_sdk_kms.types.derive_shared_secret_response


def derive_shared_secret(
    options: OperationOptions,
    input: awd_sdk_kms.types.derive_shared_secret_request.DeriveSharedSecretRequest,
) -> tuple[
    awd_sdk_kms.types.derive_shared_secret_response.DeriveSharedSecretResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_derive_shared_secret(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.derive_shared_secret_request.DeriveSharedSecretRequest,
) -> tuple[
    awd_sdk_kms.types.derive_shared_secret_response.DeriveSharedSecretResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
