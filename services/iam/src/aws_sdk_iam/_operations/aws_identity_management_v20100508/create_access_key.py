"""Generated from Smithy shape ``com.amazonaws.iam#CreateAccessKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_access_key_request
    import aws_sdk_iam.types.create_access_key_response


def create_access_key(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_access_key_request.CreateAccessKeyRequest,
) -> tuple[
    aws_sdk_iam.types.create_access_key_response.CreateAccessKeyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_access_key(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_access_key_request.CreateAccessKeyRequest,
) -> tuple[
    aws_sdk_iam.types.create_access_key_response.CreateAccessKeyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
