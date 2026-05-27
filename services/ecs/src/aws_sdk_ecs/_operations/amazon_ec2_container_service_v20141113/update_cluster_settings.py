"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateClusterSettings``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.update_cluster_settings_request
    import aws_sdk_ecs.types.update_cluster_settings_response


def update_cluster_settings(
    options: OperationOptions,
    input: aws_sdk_ecs.types.update_cluster_settings_request.UpdateClusterSettingsRequest,
) -> tuple[
    aws_sdk_ecs.types.update_cluster_settings_response.UpdateClusterSettingsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_cluster_settings(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.update_cluster_settings_request.UpdateClusterSettingsRequest,
) -> tuple[
    aws_sdk_ecs.types.update_cluster_settings_response.UpdateClusterSettingsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
