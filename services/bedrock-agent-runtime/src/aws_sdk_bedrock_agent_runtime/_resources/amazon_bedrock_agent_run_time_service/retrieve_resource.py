from typing import Optional, TYPE_CHECKING
from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import ensure_async_iterator
from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import ensure_sync_iterator
from aws_sdk_bedrock_agent_runtime._services._pipeline import OperationRequest, OperationResponse, execute_pipeline, AsyncOperationRequest, AsyncOperationResponse, aexecute_pipeline
import aws_sdk_bedrock_agent_runtime._auth._signers
import aws_sdk_bedrock_agent_runtime._auth._sigv4
if TYPE_CHECKING:
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import BedrockAgentRuntimeClient, BedrockAgentRuntimeClientConfig
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import AsyncBedrockAgentRuntimeClient, AsyncBedrockAgentRuntimeClientConfig
    import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_id
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_query
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_result
    import aws_sdk_bedrock_agent_runtime.types.next_token
    import aws_sdk_bedrock_agent_runtime.types.retrieve_request
    import aws_sdk_bedrock_agent_runtime.types.retrieve_response

class RetrieveResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service
    def retrieve(self, knowledge_base_id: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId", retrieval_query: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_query.KnowledgeBaseQuery", *, config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None, retrieval_configuration: Optional["aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"] = None, guardrail_configuration: Optional["aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"] = None, next_token: Optional["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"] = None) -> "aws_sdk_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse":
        """<p>Queries a knowledge base and retrieves information from it.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to query.</p>
            retrieval_query: <p>Contains the query to send the knowledge base.</p>
            retrieval_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>
            guardrail_configuration: <p>Guardrail settings.</p>
            next_token: <p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>
        """
        def _handler(req: 'OperationRequest[aws_sdk_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest]') -> OperationResponse["aws_sdk_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse"]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve
            output, http_response = aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve.retrieve(req.options, req.input)
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["retrieval_query"] = retrieval_query
        if retrieval_configuration is not None:
            input["retrieval_configuration"] = retrieval_configuration
        if guardrail_configuration is not None:
            input["guardrail_configuration"] = guardrail_configuration
        if next_token is not None:
            input["next_token"] = next_token

        response = execute_pipeline(OperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output

class AsyncRetrieveResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service
    async def retrieve(self, knowledge_base_id: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId", retrieval_query: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_query.KnowledgeBaseQuery", *, config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None, retrieval_configuration: Optional["aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"] = None, guardrail_configuration: Optional["aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"] = None, next_token: Optional["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"] = None) -> "aws_sdk_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse":
        """<p>Queries a knowledge base and retrieves information from it.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to query.</p>
            retrieval_query: <p>Contains the query to send the knowledge base.</p>
            retrieval_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>
            guardrail_configuration: <p>Guardrail settings.</p>
            next_token: <p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>
        """
        async def _handler(req: 'AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest]') -> AsyncOperationResponse["aws_sdk_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse"]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve
            output, http_response = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve.async_retrieve(req.options, req.input)
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest = {}  # type: ignore[typeddict-item]
        input["knowledge_base_id"] = knowledge_base_id
        input["retrieval_query"] = retrieval_query
        if retrieval_configuration is not None:
            input["retrieval_configuration"] = retrieval_configuration
        if guardrail_configuration is not None:
            input["guardrail_configuration"] = guardrail_configuration
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(AsyncOperationRequest(input=input, options=options_), handler=_handler, interceptors=list(interceptors_))
        return response.output