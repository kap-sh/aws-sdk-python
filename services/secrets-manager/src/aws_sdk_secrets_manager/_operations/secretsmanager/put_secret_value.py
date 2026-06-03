"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PutSecretValue``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.put_secret_value_request
    import aws_sdk_secrets_manager.types.put_secret_value_response


def put_secret_value(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.put_secret_value_request.PutSecretValueRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.put_secret_value_response.PutSecretValueResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_secret_value(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.put_secret_value_request.PutSecretValueRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.put_secret_value_response.PutSecretValueResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
