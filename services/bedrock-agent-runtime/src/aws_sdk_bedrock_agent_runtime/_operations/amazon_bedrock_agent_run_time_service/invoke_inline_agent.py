"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeInlineAgent``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invoke_inline_agent_request
    import aws_sdk_bedrock_agent_runtime.types.invoke_inline_agent_response


def invoke_inline_agent(
    options: OperationOptions,
    input: aws_sdk_bedrock_agent_runtime.types.invoke_inline_agent_request.InvokeInlineAgentRequest,
) -> tuple[
    aws_sdk_bedrock_agent_runtime.types.invoke_inline_agent_response.InvokeInlineAgentResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_inline_agent(
    options: AsyncOperationOptions,
    input: aws_sdk_bedrock_agent_runtime.types.invoke_inline_agent_request.InvokeInlineAgentRequest,
) -> tuple[
    aws_sdk_bedrock_agent_runtime.types.invoke_inline_agent_response.InvokeInlineAgentResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
