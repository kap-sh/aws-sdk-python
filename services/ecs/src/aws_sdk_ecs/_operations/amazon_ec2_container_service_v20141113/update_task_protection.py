"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskProtection``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.update_task_protection_request
    import aws_sdk_ecs.types.update_task_protection_response


def update_task_protection(
    options: OperationOptions,
    input: aws_sdk_ecs.types.update_task_protection_request.UpdateTaskProtectionRequest,
) -> tuple[
    aws_sdk_ecs.types.update_task_protection_response.UpdateTaskProtectionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_task_protection(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.update_task_protection_request.UpdateTaskProtectionRequest,
) -> tuple[
    aws_sdk_ecs.types.update_task_protection_response.UpdateTaskProtectionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
