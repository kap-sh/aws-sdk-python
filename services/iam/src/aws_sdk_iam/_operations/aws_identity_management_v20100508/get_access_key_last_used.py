"""Generated from Smithy shape ``com.amazonaws.iam#GetAccessKeyLastUsed``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_access_key_last_used_request
    import aws_sdk_iam.types.get_access_key_last_used_response


def get_access_key_last_used(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_access_key_last_used_request.GetAccessKeyLastUsedRequest,
) -> tuple[
    aws_sdk_iam.types.get_access_key_last_used_response.GetAccessKeyLastUsedResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_access_key_last_used(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_access_key_last_used_request.GetAccessKeyLastUsedRequest,
) -> tuple[
    aws_sdk_iam.types.get_access_key_last_used_response.GetAccessKeyLastUsedResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
