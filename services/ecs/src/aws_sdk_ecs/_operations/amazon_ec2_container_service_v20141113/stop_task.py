"""Generated from Smithy shape ``com.amazonaws.ecs#StopTask``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.stop_task_request
    import aws_sdk_ecs.types.stop_task_response


def stop_task(
    options: OperationOptions,
    input: aws_sdk_ecs.types.stop_task_request.StopTaskRequest,
) -> tuple[aws_sdk_ecs.types.stop_task_response.StopTaskResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_stop_task(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.stop_task_request.StopTaskRequest,
) -> tuple[aws_sdk_ecs.types.stop_task_response.StopTaskResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
