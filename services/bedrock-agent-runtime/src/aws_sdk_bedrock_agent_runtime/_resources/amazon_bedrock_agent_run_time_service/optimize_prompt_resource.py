from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent_runtime._auth._signers
import aws_sdk_bedrock_agent_runtime._auth._sigv4
from aws_sdk_bedrock_agent_runtime._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.input_prompt
    import aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request
    import aws_sdk_bedrock_agent_runtime.types.optimize_prompt_response
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class OptimizePromptResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    @contextmanager
    def optimize_prompt(
        self,
        input: "aws_sdk_bedrock_agent_runtime.types.input_prompt.InputPrompt",
        target_model_id: str,
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "Generator[aws_sdk_bedrock_agent_runtime.types.optimize_prompt_response.OptimizePromptResponse]":
        r"""<p>Optimizes a prompt for the task that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html\">Optimize a prompt</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            input: <p>Contains the prompt to optimize.</p>
            target_model_id: <p>The unique identifier of the model that you want to optimize the prompt for.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.optimize_prompt_response.OptimizePromptResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.optimize_prompt

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.optimize_prompt.optimize_prompt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest = {}  # type: ignore[typeddict-item]
        input_["input"] = input
        input_["target_model_id"] = target_model_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output


class AsyncOptimizePromptResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    @asynccontextmanager
    async def optimize_prompt(
        self,
        input: "aws_sdk_bedrock_agent_runtime.types.input_prompt.InputPrompt",
        target_model_id: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "AsyncGenerator[aws_sdk_bedrock_agent_runtime.types.optimize_prompt_response.OptimizePromptResponse]":
        r"""<p>Optimizes a prompt for the task that you specify. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html\">Optimize a prompt</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>

        Args:
            input: <p>Contains the prompt to optimize.</p>
            target_model_id: <p>The unique identifier of the model that you want to optimize the prompt for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.optimize_prompt_response.OptimizePromptResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.optimize_prompt

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.optimize_prompt.async_optimize_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest = {}  # type: ignore[typeddict-item]
        input_["input"] = input
        input_["target_model_id"] = target_model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        yield response.output
