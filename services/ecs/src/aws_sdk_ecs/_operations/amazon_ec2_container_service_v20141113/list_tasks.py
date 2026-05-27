"""Generated from Smithy shape ``com.amazonaws.ecs#ListTasks``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_tasks_request
    import aws_sdk_ecs.types.list_tasks_response


def list_tasks(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_tasks_request.ListTasksRequest,
) -> tuple[aws_sdk_ecs.types.list_tasks_response.ListTasksResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_tasks(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_tasks_request.ListTasksRequest,
) -> tuple[aws_sdk_ecs.types.list_tasks_response.ListTasksResponse, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
