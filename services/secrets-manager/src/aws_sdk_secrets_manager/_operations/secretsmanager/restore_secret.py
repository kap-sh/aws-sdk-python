"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RestoreSecret``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.restore_secret_request
    import aws_sdk_secrets_manager.types.restore_secret_response


def restore_secret(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.restore_secret_request.RestoreSecretRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.restore_secret_response.RestoreSecretResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_restore_secret(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.restore_secret_request.RestoreSecretRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.restore_secret_response.RestoreSecretResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
