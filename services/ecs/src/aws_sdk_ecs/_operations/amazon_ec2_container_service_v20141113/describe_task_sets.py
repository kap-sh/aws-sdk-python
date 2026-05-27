"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeTaskSets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_task_sets_request
    import aws_sdk_ecs.types.describe_task_sets_response


def describe_task_sets(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_task_sets_request.DescribeTaskSetsRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_task_sets_response.DescribeTaskSetsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_task_sets(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_task_sets_request.DescribeTaskSetsRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_task_sets_response.DescribeTaskSetsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
