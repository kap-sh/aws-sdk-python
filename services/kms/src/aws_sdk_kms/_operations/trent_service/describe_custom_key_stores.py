"""Generated from Smithy shape ``com.amazonaws.kms#DescribeCustomKeyStores``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.describe_custom_key_stores_request
    import aws_sdk_kms.types.describe_custom_key_stores_response


def describe_custom_key_stores(
    options: OperationOptions,
    input: aws_sdk_kms.types.describe_custom_key_stores_request.DescribeCustomKeyStoresRequest,
) -> tuple[
    aws_sdk_kms.types.describe_custom_key_stores_response.DescribeCustomKeyStoresResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_custom_key_stores(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.describe_custom_key_stores_request.DescribeCustomKeyStoresRequest,
) -> tuple[
    aws_sdk_kms.types.describe_custom_key_stores_response.DescribeCustomKeyStoresResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
