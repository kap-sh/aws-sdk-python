"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeContainerInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.describe_container_instances_request
    import aws_sdk_ecs.types.describe_container_instances_response


def describe_container_instances(
    options: OperationOptions,
    input: aws_sdk_ecs.types.describe_container_instances_request.DescribeContainerInstancesRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_container_instances_response.DescribeContainerInstancesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_container_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.describe_container_instances_request.DescribeContainerInstancesRequest,
) -> tuple[
    aws_sdk_ecs.types.describe_container_instances_response.DescribeContainerInstancesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
