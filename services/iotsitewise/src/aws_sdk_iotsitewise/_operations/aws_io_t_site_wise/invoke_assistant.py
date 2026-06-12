"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InvokeAssistant``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_iotsitewise._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.invoke_assistant_request
    import aws_sdk_iotsitewise.types.invoke_assistant_response


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_iotsitewise.types.invoke_assistant_request.InvokeAssistantRequest,
) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")


def invoke_assistant(
    options: OperationOptions,
    input: aws_sdk_iotsitewise.types.invoke_assistant_request.InvokeAssistantRequest,
) -> tuple[
    aws_sdk_iotsitewise.types.invoke_assistant_response.InvokeAssistantResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_assistant(
    options: AsyncOperationOptions,
    input: aws_sdk_iotsitewise.types.invoke_assistant_request.InvokeAssistantRequest,
) -> tuple[
    aws_sdk_iotsitewise.types.invoke_assistant_response.InvokeAssistantResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
