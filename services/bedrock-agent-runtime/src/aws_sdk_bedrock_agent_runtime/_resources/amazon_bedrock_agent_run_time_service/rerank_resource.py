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
    import aws_sdk_bedrock_agent_runtime.types.next_token
    import aws_sdk_bedrock_agent_runtime.types.rerank_queries_list
    import aws_sdk_bedrock_agent_runtime.types.rerank_request
    import aws_sdk_bedrock_agent_runtime.types.rerank_response
    import aws_sdk_bedrock_agent_runtime.types.rerank_result
    import aws_sdk_bedrock_agent_runtime.types.rerank_sources_list
    import aws_sdk_bedrock_agent_runtime.types.reranking_configuration
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class RerankResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def rerank(
        self,
        queries: "aws_sdk_bedrock_agent_runtime.types.rerank_queries_list.RerankQueriesList",
        sources: "aws_sdk_bedrock_agent_runtime.types.rerank_sources_list.RerankSourcesList",
        reranking_configuration: "aws_sdk_bedrock_agent_runtime.types.reranking_configuration.RerankingConfiguration",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.rerank_response.RerankResponse":
        r"""<p>Reranks the relevance of sources based on queries. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html\">Improve the relevance of query responses with a reranker model</a>.</p>

        Args:
            queries: <p>An array of objects, each of which contains information about a query to submit to the reranker model.</p>
            sources: <p>An array of objects, each of which contains information about the sources to rerank.</p>
            reranking_configuration: <p>Contains configurations for reranking.</p>
            next_token: <p>If the total number of results was greater than could fit in a response, a token is returned in the <code>nextToken</code> field. You can enter that token in this field to return the next batch of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.rerank_request.RerankRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.rerank_response.RerankResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank.rerank(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.rerank_request.RerankRequest = {}  # type: ignore[typeddict-item]
        input_["queries"] = queries
        input_["sources"] = sources
        input_["reranking_configuration"] = reranking_configuration
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRerankResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def rerank(
        self,
        queries: "aws_sdk_bedrock_agent_runtime.types.rerank_queries_list.RerankQueriesList",
        sources: "aws_sdk_bedrock_agent_runtime.types.rerank_sources_list.RerankSourcesList",
        reranking_configuration: "aws_sdk_bedrock_agent_runtime.types.reranking_configuration.RerankingConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.rerank_response.RerankResponse":
        r"""<p>Reranks the relevance of sources based on queries. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html\">Improve the relevance of query responses with a reranker model</a>.</p>

        Args:
            queries: <p>An array of objects, each of which contains information about a query to submit to the reranker model.</p>
            sources: <p>An array of objects, each of which contains information about the sources to rerank.</p>
            reranking_configuration: <p>Contains configurations for reranking.</p>
            next_token: <p>If the total number of results was greater than could fit in a response, a token is returned in the <code>nextToken</code> field. You can enter that token in this field to return the next batch of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.rerank_request.RerankRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.rerank_response.RerankResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank.async_rerank(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.rerank_request.RerankRequest = {}  # type: ignore[typeddict-item]
        input_["queries"] = queries
        input_["sources"] = sources
        input_["reranking_configuration"] = reranking_configuration
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
