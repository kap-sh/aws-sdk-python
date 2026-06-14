"""Generated from Smithy shape ``com.amazonaws.qbusiness#Chat``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_qbusiness._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.chat_input
    import aws_sdk_qbusiness.types.chat_output


def chat(
    options: OperationOptions, input: aws_sdk_qbusiness.types.chat_input.ChatInput
) -> tuple[aws_sdk_qbusiness.types.chat_output.ChatOutput, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_chat(
    options: AsyncOperationOptions, input: aws_sdk_qbusiness.types.chat_input.ChatInput
) -> tuple[aws_sdk_qbusiness.types.chat_output.ChatOutput, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")
