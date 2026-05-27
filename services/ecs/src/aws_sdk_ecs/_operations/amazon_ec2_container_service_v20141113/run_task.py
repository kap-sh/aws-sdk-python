"""Generated from Smithy shape ``com.amazonaws.ecs#RunTask``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.run_task_request
    import aws_sdk_ecs.types.run_task_response


def run_task(
    options: OperationOptions, input: aws_sdk_ecs.types.run_task_request.RunTaskRequest
) -> tuple[aws_sdk_ecs.types.run_task_response.RunTaskResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_run_task(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.run_task_request.RunTaskRequest,
) -> tuple[aws_sdk_ecs.types.run_task_response.RunTaskResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
