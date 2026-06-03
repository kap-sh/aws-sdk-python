"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetRandomPassword``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.get_random_password_request
    import aws_sdk_secrets_manager.types.get_random_password_response


def get_random_password(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.get_random_password_request.GetRandomPasswordRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.get_random_password_response.GetRandomPasswordResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_random_password(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.get_random_password_request.GetRandomPasswordRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.get_random_password_response.GetRandomPasswordResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
