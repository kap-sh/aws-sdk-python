"""Generated from Smithy shape ``com.amazonaws.kms#DescribeKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.describe_key_request
    import awd_sdk_kms.types.describe_key_response


def describe_key(
    options: OperationOptions,
    input: awd_sdk_kms.types.describe_key_request.DescribeKeyRequest,
) -> tuple[
    awd_sdk_kms.types.describe_key_response.DescribeKeyResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_key(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.describe_key_request.DescribeKeyRequest,
) -> tuple[
    awd_sdk_kms.types.describe_key_response.DescribeKeyResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
