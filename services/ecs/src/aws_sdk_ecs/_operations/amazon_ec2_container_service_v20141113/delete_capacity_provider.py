"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteCapacityProvider``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.delete_capacity_provider_request
    import aws_sdk_ecs.types.delete_capacity_provider_response


def delete_capacity_provider(
    options: OperationOptions,
    input: aws_sdk_ecs.types.delete_capacity_provider_request.DeleteCapacityProviderRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_capacity_provider_response.DeleteCapacityProviderResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_capacity_provider(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.delete_capacity_provider_request.DeleteCapacityProviderRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_capacity_provider_response.DeleteCapacityProviderResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
