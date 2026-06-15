"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeCodeInterpreter``."""

from __future__ import annotations

from typing import TYPE_CHECKING

import zapros

from aws_sdk_bedrock_agentcore._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_request
    import aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_response


def invoke_code_interpreter(
    options: OperationOptions,
    input: aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_request.InvokeCodeInterpreterRequest,
) -> tuple[
    aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_response.InvokeCodeInterpreterResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_invoke_code_interpreter(
    options: AsyncOperationOptions,
    input: aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_request.InvokeCodeInterpreterRequest,
) -> tuple[
    aws_sdk_bedrock_agentcore.types.invoke_code_interpreter_response.InvokeCodeInterpreterResponse,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
