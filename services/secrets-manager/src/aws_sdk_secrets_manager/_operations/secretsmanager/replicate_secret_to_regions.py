"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicateSecretToRegions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.replicate_secret_to_regions_request
    import aws_sdk_secrets_manager.types.replicate_secret_to_regions_response


def replicate_secret_to_regions(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.replicate_secret_to_regions_request.ReplicateSecretToRegionsRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.replicate_secret_to_regions_response.ReplicateSecretToRegionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_replicate_secret_to_regions(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.replicate_secret_to_regions_request.ReplicateSecretToRegionsRequest,
) -> tuple[
    aws_sdk_secrets_manager.types.replicate_secret_to_regions_response.ReplicateSecretToRegionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
