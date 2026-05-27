"""Generated from Smithy shape ``com.amazonaws.ec2#CreateStoreImageTask``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_store_image_task_request
    import aws_sdk_ec2.types.create_store_image_task_result


def create_store_image_task(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_store_image_task_request.CreateStoreImageTaskRequest,
) -> tuple[
    aws_sdk_ec2.types.create_store_image_task_result.CreateStoreImageTaskResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_store_image_task(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_store_image_task_request.CreateStoreImageTaskRequest,
) -> tuple[
    aws_sdk_ec2.types.create_store_image_task_result.CreateStoreImageTaskResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
