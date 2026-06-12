"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizePrompt``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
from aws_sdk_bedrock_agent_runtime._services._pipeline import AsyncOperationOptions, OperationOptions
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request
    import aws_sdk_bedrock_agent_runtime.types.optimize_prompt_response

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")

def optimize_prompt(options: OperationOptions, input: aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest) -> tuple[aws_sdk_bedrock_agent_runtime.types.optimize_prompt_response.OptimizePromptResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")

async def async_optimize_prompt(options: AsyncOperationOptions, input: aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest) -> tuple[aws_sdk_bedrock_agent_runtime.types.optimize_prompt_response.OptimizePromptResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")