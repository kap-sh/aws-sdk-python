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
    import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_id
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_query
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration
    import aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_result
    import aws_sdk_bedrock_agent_runtime.types.next_token
    import aws_sdk_bedrock_agent_runtime.types.retrieve_request
    import aws_sdk_bedrock_agent_runtime.types.retrieve_response
    from aws_sdk_bedrock_agent_runtime._services.async_bedrock_agent_runtime import (
        AsyncBedrockAgentRuntimeClient,
        AsyncBedrockAgentRuntimeClientConfig,
    )
    from aws_sdk_bedrock_agent_runtime._services.bedrock_agent_runtime import (
        BedrockAgentRuntimeClient,
        BedrockAgentRuntimeClientConfig,
    )


class RetrieveResource:
    def __init__(self, service: BedrockAgentRuntimeClient) -> None:
        self._service = service

    def retrieve(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId",
        retrieval_query: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_query.KnowledgeBaseQuery",
        *,
        config_overrides: Optional[BedrockAgentRuntimeClientConfig] = None,
        retrieval_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse":
        r"""<p>Queries a knowledge base and retrieves information from it.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to query.</p>
            retrieval_query: <p>Contains the query to send the knowledge base.</p>
            retrieval_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>
            guardrail_configuration: <p>Guardrail settings.</p>
            next_token: <p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>

        Raises:
            aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve

            output, http_response = (
                aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve.retrieve(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["retrieval_query"] = retrieval_query
        if retrieval_configuration is not None:
            input_["retrieval_configuration"] = retrieval_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRetrieveResource:
    def __init__(self, service: AsyncBedrockAgentRuntimeClient) -> None:
        self._service = service

    async def retrieve(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_id.KnowledgeBaseId",
        retrieval_query: "aws_sdk_bedrock_agent_runtime.types.knowledge_base_query.KnowledgeBaseQuery",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        retrieval_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "aws_sdk_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        next_token: Optional[
            "aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse":
        r"""<p>Queries a knowledge base and retrieves information from it.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to query.</p>
            retrieval_query: <p>Contains the query to send the knowledge base.</p>
            retrieval_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html\">Query configurations</a>.</p>
            guardrail_configuration: <p>Guardrail settings.</p>
            next_token: <p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>

        Raises:
            aws_sdk_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            aws_sdk_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            aws_sdk_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            aws_sdk_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            aws_sdk_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse"
        ]:
            import aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve.async_retrieve(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["retrieval_query"] = retrieval_query
        if retrieval_configuration is not None:
            input_["retrieval_configuration"] = retrieval_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
