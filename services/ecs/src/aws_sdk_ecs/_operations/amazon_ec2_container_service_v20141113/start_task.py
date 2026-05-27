"""Generated from Smithy shape ``com.amazonaws.ecs#StartTask``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.start_task_request
    import aws_sdk_ecs.types.start_task_response


def start_task(
    options: OperationOptions,
    input: aws_sdk_ecs.types.start_task_request.StartTaskRequest,
) -> tuple[aws_sdk_ecs.types.start_task_response.StartTaskResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_start_task(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.start_task_request.StartTaskRequest,
) -> tuple[aws_sdk_ecs.types.start_task_response.StartTaskResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
