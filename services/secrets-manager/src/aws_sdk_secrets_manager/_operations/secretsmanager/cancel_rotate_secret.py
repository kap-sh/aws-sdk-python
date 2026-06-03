"""Generated from Smithy shape ``com.amazonaws.secretsmanager#CancelRotateSecret``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.cancel_rotate_secret_request
    import aws_sdk_secrets_manager.types.cancel_rotate_secret_response


def cancel_rotate_secret(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.cancel_rotate_secret_request.CancelRotateSecretRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.cancel_rotate_secret_response.CancelRotateSecretResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_cancel_rotate_secret(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.cancel_rotate_secret_request.CancelRotateSecretRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.cancel_rotate_secret_response.CancelRotateSecretResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
