"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListSecretVersionIds``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.list_secret_version_ids_request
    import aws_sdk_secrets_manager.types.list_secret_version_ids_response


def list_secret_version_ids(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.list_secret_version_ids_request.ListSecretVersionIdsRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.list_secret_version_ids_response.ListSecretVersionIdsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_secret_version_ids(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.list_secret_version_ids_request.ListSecretVersionIdsRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.list_secret_version_ids_response.ListSecretVersionIdsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
