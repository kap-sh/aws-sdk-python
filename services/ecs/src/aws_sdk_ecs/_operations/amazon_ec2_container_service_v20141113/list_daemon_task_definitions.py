"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonTaskDefinitions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.list_daemon_task_definitions_request
    import aws_sdk_ecs.types.list_daemon_task_definitions_response


def list_daemon_task_definitions(
    options: OperationOptions,
    input: aws_sdk_ecs.types.list_daemon_task_definitions_request.ListDaemonTaskDefinitionsRequest,
) -> tuple[
    aws_sdk_ecs.types.list_daemon_task_definitions_response.ListDaemonTaskDefinitionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_daemon_task_definitions(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.list_daemon_task_definitions_request.ListDaemonTaskDefinitionsRequest,
) -> tuple[
    aws_sdk_ecs.types.list_daemon_task_definitions_response.ListDaemonTaskDefinitionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
