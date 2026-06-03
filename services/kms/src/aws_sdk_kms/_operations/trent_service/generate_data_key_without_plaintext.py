"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKeyWithoutPlaintext``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.generate_data_key_without_plaintext_request
    import aws_sdk_kms.types.generate_data_key_without_plaintext_response


def generate_data_key_without_plaintext(
    options: OperationOptions,
    input: aws_sdk_kms.types.generate_data_key_without_plaintext_request.GenerateDataKeyWithoutPlaintextRequest,
) -> tuple[
    aws_sdk_kms.types.generate_data_key_without_plaintext_response.GenerateDataKeyWithoutPlaintextResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_generate_data_key_without_plaintext(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.generate_data_key_without_plaintext_request.GenerateDataKeyWithoutPlaintextRequest,
) -> tuple[
    aws_sdk_kms.types.generate_data_key_without_plaintext_response.GenerateDataKeyWithoutPlaintextResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
