"""Generated from Smithy shape ``com.amazonaws.ecs#CreateDaemon``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.create_daemon_request
    import aws_sdk_ecs.types.create_daemon_response


def create_daemon(
    options: OperationOptions,
    input: aws_sdk_ecs.types.create_daemon_request.CreateDaemonRequest,
) -> tuple[
    aws_sdk_ecs.types.create_daemon_response.CreateDaemonResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_daemon(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.create_daemon_request.CreateDaemonRequest,
) -> tuple[
    aws_sdk_ecs.types.create_daemon_response.CreateDaemonResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
