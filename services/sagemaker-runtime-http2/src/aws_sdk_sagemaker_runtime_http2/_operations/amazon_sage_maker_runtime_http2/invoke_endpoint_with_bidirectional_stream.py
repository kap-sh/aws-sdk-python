"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#InvokeEndpointWithBidirectionalStream``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_sagemaker_runtime_http2._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input
    import aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output


def invoke_endpoint_with_bidirectional_stream(
    options: OperationOptions,
    input: aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input.InvokeEndpointWithBidirectionalStreamInput,
) -> tuple[
    aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_endpoint_with_bidirectional_stream(
    options: AsyncOperationOptions,
    input: aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_input.InvokeEndpointWithBidirectionalStreamInput,
) -> tuple[
    aws_sdk_sagemaker_runtime_http2.types.invoke_endpoint_with_bidirectional_stream_output.InvokeEndpointWithBidirectionalStreamOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
