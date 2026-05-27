"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateContainerInstancesState``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.update_container_instances_state_request
    import aws_sdk_ecs.types.update_container_instances_state_response


def update_container_instances_state(
    options: OperationOptions,
    input: aws_sdk_ecs.types.update_container_instances_state_request.UpdateContainerInstancesStateRequest,
) -> tuple[
    aws_sdk_ecs.types.update_container_instances_state_response.UpdateContainerInstancesStateResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_container_instances_state(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.update_container_instances_state_request.UpdateContainerInstancesStateRequest,
) -> tuple[
    aws_sdk_ecs.types.update_container_instances_state_response.UpdateContainerInstancesStateResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
