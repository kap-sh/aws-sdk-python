"""Generated from Smithy shape ``com.amazonaws.ecs#GetTaskProtection``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.get_task_protection_request
    import aws_sdk_ecs.types.get_task_protection_response


def get_task_protection(
    options: OperationOptions,
    input: aws_sdk_ecs.types.get_task_protection_request.GetTaskProtectionRequest,
) -> tuple[
    aws_sdk_ecs.types.get_task_protection_response.GetTaskProtectionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_task_protection(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.get_task_protection_request.GetTaskProtectionRequest,
) -> tuple[
    aws_sdk_ecs.types.get_task_protection_response.GetTaskProtectionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
