"""Generated from Smithy shape ``com.amazonaws.secretsmanager#CreateSecret``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.create_secret_request
    import aws_sdk_secrets_manager.types.create_secret_response


def create_secret(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.create_secret_request.CreateSecretRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.create_secret_response.CreateSecretResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_secret(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.create_secret_request.CreateSecretRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.create_secret_response.CreateSecretResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
