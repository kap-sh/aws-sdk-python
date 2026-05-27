"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemon``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.delete_daemon_request
    import aws_sdk_ecs.types.delete_daemon_response


def delete_daemon(
    options: OperationOptions,
    input: aws_sdk_ecs.types.delete_daemon_request.DeleteDaemonRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_daemon_response.DeleteDaemonResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_daemon(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.delete_daemon_request.DeleteDaemonRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_daemon_response.DeleteDaemonResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
