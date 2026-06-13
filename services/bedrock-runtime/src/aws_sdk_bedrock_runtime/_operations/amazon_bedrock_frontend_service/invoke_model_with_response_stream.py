"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithResponseStream``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_bedrock_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.invoke_model_with_response_stream_request
    import aws_sdk_bedrock_runtime.types.invoke_model_with_response_stream_response


def invoke_model_with_response_stream(
    options: OperationOptions,
    input: aws_sdk_bedrock_runtime.types.invoke_model_with_response_stream_request.InvokeModelWithResponseStreamRequest,
) -> tuple[
    aws_sdk_bedrock_runtime.types.invoke_model_with_response_stream_response.InvokeModelWithResponseStreamResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_model_with_response_stream(
    options: AsyncOperationOptions,
    input: aws_sdk_bedrock_runtime.types.invoke_model_with_response_stream_request.InvokeModelWithResponseStreamRequest,
) -> tuple[
    aws_sdk_bedrock_runtime.types.invoke_model_with_response_stream_response.InvokeModelWithResponseStreamResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
