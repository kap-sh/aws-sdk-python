"""Generated from Smithy shape ``com.amazonaws.secretsmanager#UpdateSecretVersionStage``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.update_secret_version_stage_request
    import aws_sdk_secrets_manager.types.update_secret_version_stage_response


def update_secret_version_stage(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.update_secret_version_stage_request.UpdateSecretVersionStageRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.update_secret_version_stage_response.UpdateSecretVersionStageResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_secret_version_stage(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.update_secret_version_stage_request.UpdateSecretVersionStageRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.update_secret_version_stage_response.UpdateSecretVersionStageResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
