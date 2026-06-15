"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarness``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_bedrock_agentcore._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.invoke_harness_request
    import aws_sdk_bedrock_agentcore.types.invoke_harness_response


def invoke_harness(
    options: OperationOptions,
    input: aws_sdk_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest,
) -> tuple[
    aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_harness(
    options: AsyncOperationOptions,
    input: aws_sdk_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest,
) -> tuple[
    aws_sdk_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
