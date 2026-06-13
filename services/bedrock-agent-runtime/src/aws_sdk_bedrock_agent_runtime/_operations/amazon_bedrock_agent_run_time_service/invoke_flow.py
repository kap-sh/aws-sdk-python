"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeFlow``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.invoke_flow_request
    import aws_sdk_bedrock_agent_runtime.types.invoke_flow_response


def invoke_flow(
    options: OperationOptions,
    input: aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest,
) -> tuple[
    aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_flow(
    options: AsyncOperationOptions,
    input: aws_sdk_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest,
) -> tuple[
    aws_sdk_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
