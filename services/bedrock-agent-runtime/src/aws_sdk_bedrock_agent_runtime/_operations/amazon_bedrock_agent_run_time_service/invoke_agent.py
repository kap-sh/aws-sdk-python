"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeAgent``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
from aws_sdk_bedrock_agent_runtime._services._pipeline import AsyncOperationOptions, OperationOptions
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invoke_agent_request
    import aws_sdk_bedrock_agent_runtime.types.invoke_agent_response

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")

def invoke_agent(options: OperationOptions, input: aws_sdk_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest) -> tuple[aws_sdk_bedrock_agent_runtime.types.invoke_agent_response.InvokeAgentResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")

async def async_invoke_agent(options: AsyncOperationOptions, input: aws_sdk_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest) -> tuple[aws_sdk_bedrock_agent_runtime.types.invoke_agent_response.InvokeAgentResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")