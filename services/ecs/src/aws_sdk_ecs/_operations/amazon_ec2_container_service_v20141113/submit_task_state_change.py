"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitTaskStateChange``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.submit_task_state_change_request
    import aws_sdk_ecs.types.submit_task_state_change_response


def submit_task_state_change(
    options: OperationOptions,
    input: aws_sdk_ecs.types.submit_task_state_change_request.SubmitTaskStateChangeRequest,
) -> tuple[
    aws_sdk_ecs.types.submit_task_state_change_response.SubmitTaskStateChangeResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_submit_task_state_change(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.submit_task_state_change_request.SubmitTaskStateChangeRequest,
) -> tuple[
    aws_sdk_ecs.types.submit_task_state_change_response.SubmitTaskStateChangeResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
