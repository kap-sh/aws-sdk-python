"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyLastUsage``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.get_key_last_usage_request
    import aws_sdk_kms.types.get_key_last_usage_response


def get_key_last_usage(
    options: OperationOptions,
    input: aws_sdk_kms.types.get_key_last_usage_request.GetKeyLastUsageRequest,
) -> tuple[
    aws_sdk_kms.types.get_key_last_usage_response.GetKeyLastUsageResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_key_last_usage(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.get_key_last_usage_request.GetKeyLastUsageRequest,
) -> tuple[
    aws_sdk_kms.types.get_key_last_usage_response.GetKeyLastUsageResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
