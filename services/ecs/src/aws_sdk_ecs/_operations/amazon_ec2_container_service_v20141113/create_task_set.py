"""Generated from Smithy shape ``com.amazonaws.ecs#CreateTaskSet``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.create_task_set_request
    import aws_sdk_ecs.types.create_task_set_response


def create_task_set(
    options: OperationOptions,
    input: aws_sdk_ecs.types.create_task_set_request.CreateTaskSetRequest,
) -> tuple[
    aws_sdk_ecs.types.create_task_set_response.CreateTaskSetResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_task_set(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.create_task_set_request.CreateTaskSetRequest,
) -> tuple[
    aws_sdk_ecs.types.create_task_set_response.CreateTaskSetResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
