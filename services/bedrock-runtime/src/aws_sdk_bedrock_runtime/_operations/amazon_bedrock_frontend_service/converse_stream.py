"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStream``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
from aws_sdk_bedrock_runtime._services._pipeline import AsyncOperationOptions, OperationOptions
if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.converse_stream_request
    import aws_sdk_bedrock_runtime.types.converse_stream_response

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")

def converse_stream(options: OperationOptions, input: aws_sdk_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest) -> tuple[aws_sdk_bedrock_runtime.types.converse_stream_response.ConverseStreamResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")

async def async_converse_stream(options: AsyncOperationOptions, input: aws_sdk_bedrock_runtime.types.converse_stream_request.ConverseStreamRequest) -> tuple[aws_sdk_bedrock_runtime.types.converse_stream_response.ConverseStreamResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")