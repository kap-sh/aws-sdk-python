"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKeyPair``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.generate_data_key_pair_request
    import awd_sdk_kms.types.generate_data_key_pair_response


def generate_data_key_pair(
    options: OperationOptions,
    input: awd_sdk_kms.types.generate_data_key_pair_request.GenerateDataKeyPairRequest,
) -> tuple[
    awd_sdk_kms.types.generate_data_key_pair_response.GenerateDataKeyPairResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_generate_data_key_pair(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.generate_data_key_pair_request.GenerateDataKeyPairRequest,
) -> tuple[
    awd_sdk_kms.types.generate_data_key_pair_response.GenerateDataKeyPairResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
