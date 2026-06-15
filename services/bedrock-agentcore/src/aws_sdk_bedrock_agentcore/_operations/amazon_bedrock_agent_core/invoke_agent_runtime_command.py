"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeAgentRuntimeCommand``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_bedrock_agentcore._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request
    import aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_response


def invoke_agent_runtime_command(
    options: OperationOptions,
    input: aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request.InvokeAgentRuntimeCommandRequest,
) -> tuple[
    aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_response.InvokeAgentRuntimeCommandResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_agent_runtime_command(
    options: AsyncOperationOptions,
    input: aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_request.InvokeAgentRuntimeCommandRequest,
) -> tuple[
    aws_sdk_bedrock_agentcore.types.invoke_agent_runtime_command_response.InvokeAgentRuntimeCommandResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
