"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StartConversation``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_lex_runtime_v2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.start_conversation_request
    import aws_sdk_lex_runtime_v2.types.start_conversation_response


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_lex_runtime_v2.types.start_conversation_request.StartConversationRequest,
) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")


def start_conversation(
    options: OperationOptions,
    input: aws_sdk_lex_runtime_v2.types.start_conversation_request.StartConversationRequest,
) -> tuple[
    aws_sdk_lex_runtime_v2.types.start_conversation_response.StartConversationResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_start_conversation(
    options: AsyncOperationOptions,
    input: aws_sdk_lex_runtime_v2.types.start_conversation_request.StartConversationRequest,
) -> tuple[
    aws_sdk_lex_runtime_v2.types.start_conversation_response.StartConversationResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
