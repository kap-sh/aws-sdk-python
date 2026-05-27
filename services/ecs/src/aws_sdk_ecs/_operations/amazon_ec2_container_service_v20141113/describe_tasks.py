"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTasks``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_tasks_request
    import aws_sdk_ecs.types.describe_tasks_response


def describe_tasks(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_tasks_request.DescribeTasksRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_tasks_response.DescribeTasksResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_tasks(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_tasks_request.DescribeTasksRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_tasks_response.DescribeTasksResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
