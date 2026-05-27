"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommand``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.execute_command_request
    import aws_sdk_ecs.types.execute_command_response


def execute_command(
    options: OperationOptions,
    input: aws_sdk_ecs.types.execute_command_request.ExecuteCommandRequest,
) -> tuple[
    aws_sdk_ecs.types.execute_command_response.ExecuteCommandResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_execute_command(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.execute_command_request.ExecuteCommandRequest,
) -> tuple[
    aws_sdk_ecs.types.execute_command_response.ExecuteCommandResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
