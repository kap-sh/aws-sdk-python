"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessage``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_devops_agent._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.send_message_request
    import aws_sdk_devops_agent.types.send_message_response


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_devops_agent.types.send_message_request.SendMessageRequest,
) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")


def send_message(
    options: OperationOptions,
    input: aws_sdk_devops_agent.types.send_message_request.SendMessageRequest,
) -> tuple[
    aws_sdk_devops_agent.types.send_message_response.SendMessageResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_send_message(
    options: AsyncOperationOptions,
    input: aws_sdk_devops_agent.types.send_message_request.SendMessageRequest,
) -> tuple[
    aws_sdk_devops_agent.types.send_message_response.SendMessageResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
