"""Generated from Smithy shape ``com.amazonaws.iam#ListAccessKeys``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_access_keys_request
    import aws_sdk_iam.types.list_access_keys_response


def list_access_keys(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_access_keys_request.ListAccessKeysRequest,
) -> tuple[
    aws_sdk_iam.types.list_access_keys_response.ListAccessKeysResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_access_keys(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_access_keys_request.ListAccessKeysRequest,
) -> tuple[
    aws_sdk_iam.types.list_access_keys_response.ListAccessKeysResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
