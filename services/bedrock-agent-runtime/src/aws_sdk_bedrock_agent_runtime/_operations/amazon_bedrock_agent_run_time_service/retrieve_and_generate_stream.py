"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateStream``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
from aws_sdk_bedrock_agent_runtime._services._pipeline import AsyncOperationOptions, OperationOptions
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request
    import aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")

def retrieve_and_generate_stream(options: OperationOptions, input: aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest) -> tuple[aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")

async def async_retrieve_and_generate_stream(options: AsyncOperationOptions, input: aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest) -> tuple[aws_sdk_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")