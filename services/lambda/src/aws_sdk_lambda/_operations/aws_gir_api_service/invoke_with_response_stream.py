"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeWithResponseStream``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_lambda._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_lambda.types.invoke_with_response_stream_request
    import aws_sdk_lambda.types.invoke_with_response_stream_response


def invoke_with_response_stream(
    options: OperationOptions,
    input: aws_sdk_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest,
) -> tuple[
    aws_sdk_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_with_response_stream(
    options: AsyncOperationOptions,
    input: aws_sdk_lambda.types.invoke_with_response_stream_request.InvokeWithResponseStreamRequest,
) -> tuple[
    aws_sdk_lambda.types.invoke_with_response_stream_response.InvokeWithResponseStreamResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
