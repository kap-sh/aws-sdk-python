"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterTaskDefinition``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.register_task_definition_request
    import aws_sdk_ecs.types.register_task_definition_response


def register_task_definition(
    options: OperationOptions,
    input: aws_sdk_ecs.types.register_task_definition_request.RegisterTaskDefinitionRequest,
) -> tuple[
    aws_sdk_ecs.types.register_task_definition_response.RegisterTaskDefinitionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_register_task_definition(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.register_task_definition_request.RegisterTaskDefinitionRequest,
) -> tuple[
    aws_sdk_ecs.types.register_task_definition_response.RegisterTaskDefinitionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
