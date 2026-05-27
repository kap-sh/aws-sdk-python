"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskSet``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.update_task_set_request
    import aws_sdk_ecs.types.update_task_set_response


def update_task_set(
    options: OperationOptions,
    input: aws_sdk_ecs.types.update_task_set_request.UpdateTaskSetRequest,
) -> tuple[
    aws_sdk_ecs.types.update_task_set_response.UpdateTaskSetResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_task_set(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.update_task_set_request.UpdateTaskSetRequest,
) -> tuple[
    aws_sdk_ecs.types.update_task_set_response.UpdateTaskSetResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
