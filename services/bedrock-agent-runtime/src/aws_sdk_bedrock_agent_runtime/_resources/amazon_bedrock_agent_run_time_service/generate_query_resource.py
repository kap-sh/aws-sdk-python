from __future__ import annotations

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
    import aws_sdk_bedrock_agent_runtime.types.generate_query_request
    import aws_sdk_bedrock_agent_runtime.types.generate_query_response
    import aws_sdk_bedrock_agent_runtime.types.query_generation_input
    import aws_sdk_bedrock_agent_runtime.types.transformation_configuration
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class GenerateQueryResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def generate_query(
        self,
        query_generation_input: "aws_sdk_bedrock_agent_runtime.types.query_generation_input.QueryGenerationInput",
        transformation_configuration: "aws_sdk_bedrock_agent_runtime.types.transformation_configuration.TransformationConfiguration",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse":
        r"""<p>Generates an SQL query from a natural language query. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-generate-query.html\">Generate a query for structured data</a> in the Amazon Bedrock User Guide.</p>

        Args:
            query_generation_input: <p>Specifies information about a natural language query to transform into SQL.</p>
            transformation_configuration: <p>Specifies configurations for transforming the natural language query into SQL.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query.generate_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest = {}  # type: ignore[typeddict-item]
        input_["query_generation_input"] = query_generation_input
        input_["transformation_configuration"] = transformation_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGenerateQueryResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def generate_query(
        self,
        query_generation_input: "aws_sdk_bedrock_agent_runtime.types.query_generation_input.QueryGenerationInput",
        transformation_configuration: "aws_sdk_bedrock_agent_runtime.types.transformation_configuration.TransformationConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse":
        r"""<p>Generates an SQL query from a natural language query. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-generate-query.html\">Generate a query for structured data</a> in the Amazon Bedrock User Guide.</p>

        Args:
            query_generation_input: <p>Specifies information about a natural language query to transform into SQL.</p>
            transformation_configuration: <p>Specifies configurations for transforming the natural language query into SQL.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query.async_generate_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest = {}  # type: ignore[typeddict-item]
        input_["query_generation_input"] = query_generation_input
        input_["transformation_configuration"] = transformation_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
