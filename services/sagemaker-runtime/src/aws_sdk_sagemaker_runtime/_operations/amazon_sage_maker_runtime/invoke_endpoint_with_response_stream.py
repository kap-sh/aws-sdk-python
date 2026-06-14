"""Generated from Smithy shape ``com.amazonaws.sagemakerruntime#InvokeEndpointWithResponseStream``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_sagemaker_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input
    import aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output


def invoke_endpoint_with_response_stream(
    options: OperationOptions,
    input: aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input.InvokeEndpointWithResponseStreamInput,
) -> tuple[
    aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_endpoint_with_response_stream(
    options: AsyncOperationOptions,
    input: aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_input.InvokeEndpointWithResponseStreamInput,
) -> tuple[
    aws_sdk_sagemaker_runtime.types.invoke_endpoint_with_response_stream_output.InvokeEndpointWithResponseStreamOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
