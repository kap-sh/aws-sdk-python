"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecrets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.list_secrets_request
    import aws_sdk_secrets_manager.types.list_secrets_response


def list_secrets(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.list_secrets_request.ListSecretsRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.list_secrets_response.ListSecretsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_secrets(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.list_secrets_request.ListSecretsRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.list_secrets_response.ListSecretsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
