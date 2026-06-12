"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStream``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
from aws_sdk_bedrock_runtime._services._pipeline import AsyncOperationOptions, OperationOptions
if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request
    import aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response

def build_request(options: OperationOptions | AsyncOperationOptions, input: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")

def invoke_model_with_bidirectional_stream(options: OperationOptions, input: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest) -> tuple[aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")

async def async_invoke_model_with_bidirectional_stream(options: AsyncOperationOptions, input: aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_request.InvokeModelWithBidirectionalStreamRequest) -> tuple[aws_sdk_bedrock_runtime.types.invoke_model_with_bidirectional_stream_response.InvokeModelWithBidirectionalStreamResponse, zapros.Response]:
    raise NotImplementedError("event stream output is not yet supported")