"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonTaskDefinition``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.delete_daemon_task_definition_request
    import aws_sdk_ecs.types.delete_daemon_task_definition_response


def delete_daemon_task_definition(
    options: OperationOptions,
    input: aws_sdk_ecs.types.delete_daemon_task_definition_request.DeleteDaemonTaskDefinitionRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_daemon_task_definition_response.DeleteDaemonTaskDefinitionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_daemon_task_definition(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.delete_daemon_task_definition_request.DeleteDaemonTaskDefinitionRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_daemon_task_definition_response.DeleteDaemonTaskDefinitionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
