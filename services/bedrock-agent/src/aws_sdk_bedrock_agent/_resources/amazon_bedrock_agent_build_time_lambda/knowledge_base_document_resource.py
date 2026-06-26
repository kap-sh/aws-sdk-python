from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agent._auth._signers
import aws_sdk_bedrock_agent._auth._sigv4
from aws_sdk_bedrock_agent._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_request
    import aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_response
    import aws_sdk_bedrock_agent.types.document_identifiers
    import aws_sdk_bedrock_agent.types.get_knowledge_base_documents_request
    import aws_sdk_bedrock_agent.types.get_knowledge_base_documents_response
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_request
    import aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_response
    import aws_sdk_bedrock_agent.types.knowledge_base_document_detail
    import aws_sdk_bedrock_agent.types.knowledge_base_documents
    import aws_sdk_bedrock_agent.types.list_knowledge_base_documents_request
    import aws_sdk_bedrock_agent.types.list_knowledge_base_documents_response
    import aws_sdk_bedrock_agent.types.max_results
    import aws_sdk_bedrock_agent.types.next_token
    from aws_sdk_bedrock_agent._services.async_bedrock_agent import (
        AsyncBedrockAgentClient,
        AsyncBedrockAgentClientConfig,
    )
    from aws_sdk_bedrock_agent._services.bedrock_agent import (
        BedrockAgentClient,
        BedrockAgentClientConfig,
    )


class KnowledgeBaseDocumentResource:
    def __init__(self, service: BedrockAgentClient) -> None:
        self._service = service

    def delete_knowledge_base_documents(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        document_identifiers: "aws_sdk_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse":
        r"""<p>Deletes documents from a data source and syncs the changes to the knowledge base that is connected to it. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html\">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document to delete.</p>

        Raises:
            aws_sdk_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents.delete_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["data_source_id"] = data_source_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["document_identifiers"] = document_identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_knowledge_base_documents(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        document_identifiers: "aws_sdk_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse":
        r"""<p>Retrieves specific documents from a data source that is connected to a knowledge base. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html\">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document for which to retrieve information.</p>

        Raises:
            aws_sdk_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents.get_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["data_source_id"] = data_source_id
        input_["document_identifiers"] = document_identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def ingest_knowledge_base_documents(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        documents: "aws_sdk_bedrock_agent.types.knowledge_base_documents.KnowledgeBaseDocuments",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse":
        r"""<p>Ingests documents directly into the knowledge base that is connected to the data source. The <code>dataSourceType</code> specified in the content for each document must match the type of the data source that you specify in the header. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html\">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to ingest the documents into.</p>
            data_source_id: <p>The unique identifier of the data source connected to the knowledge base that you're adding documents to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            documents: <p>A list of objects, each of which contains information about the documents to add.</p>

        Raises:
            aws_sdk_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents.ingest_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["data_source_id"] = data_source_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["documents"] = documents

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_knowledge_base_documents(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[BedrockAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse":
        r"""<p>Retrieves all the documents contained in a data source that is connected to a knowledge base. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html\">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            aws_sdk_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents

            output, http_response = (
                aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents.list_knowledge_base_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["data_source_id"] = data_source_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncKnowledgeBaseDocumentResource:
    def __init__(self, service: AsyncBedrockAgentClient) -> None:
        self._service = service

    async def delete_knowledge_base_documents(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        document_identifiers: "aws_sdk_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse":
        r"""<p>Deletes documents from a data source and syncs the changes to the knowledge base that is connected to it. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html\">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document to delete.</p>

        Raises:
            aws_sdk_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_response.DeleteKnowledgeBaseDocumentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.delete_knowledge_base_documents.async_delete_knowledge_base_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.delete_knowledge_base_documents_request.DeleteKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["data_source_id"] = data_source_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["document_identifiers"] = document_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_knowledge_base_documents(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        document_identifiers: "aws_sdk_bedrock_agent.types.document_identifiers.DocumentIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
    ) -> "aws_sdk_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse":
        r"""<p>Retrieves specific documents from a data source that is connected to a knowledge base. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html\">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            document_identifiers: <p>A list of objects, each of which contains information to identify a document for which to retrieve information.</p>

        Raises:
            aws_sdk_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.get_knowledge_base_documents_response.GetKnowledgeBaseDocumentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.get_knowledge_base_documents.async_get_knowledge_base_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.get_knowledge_base_documents_request.GetKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["data_source_id"] = data_source_id
        input_["document_identifiers"] = document_identifiers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def ingest_knowledge_base_documents(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        documents: "aws_sdk_bedrock_agent.types.knowledge_base_documents.KnowledgeBaseDocuments",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        client_token: Optional[
            "aws_sdk_bedrock_agent.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse":
        r"""<p>Ingests documents directly into the knowledge base that is connected to the data source. The <code>dataSourceType</code> specified in the content for each document must match the type of the data source that you specify in the header. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html\">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to ingest the documents into.</p>
            data_source_id: <p>The unique identifier of the data source connected to the knowledge base that you're adding documents to.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>
            documents: <p>A list of objects, each of which contains information about the documents to add.</p>

        Raises:
            aws_sdk_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_response.IngestKnowledgeBaseDocumentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.ingest_knowledge_base_documents.async_ingest_knowledge_base_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.ingest_knowledge_base_documents_request.IngestKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["data_source_id"] = data_source_id
        if client_token is not None:
            input_["client_token"] = client_token
        input_["documents"] = documents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_knowledge_base_documents(
        self,
        knowledge_base_id: "aws_sdk_bedrock_agent.types.id.Id",
        data_source_id: "aws_sdk_bedrock_agent.types.id.Id",
        *,
        config_overrides: Optional[AsyncBedrockAgentClientConfig] = None,
        max_results: Optional[
            "aws_sdk_bedrock_agent.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_bedrock_agent.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse":
        r"""<p>Retrieves all the documents contained in a data source that is connected to a knowledge base. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html\">Ingest changes directly into a knowledge base</a> in the Amazon Bedrock User Guide.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that is connected to the data source.</p>
            data_source_id: <p>The unique identifier of the data source that contains the documents.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            aws_sdk_bedrock_agent.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            aws_sdk_bedrock_agent.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            aws_sdk_bedrock_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            aws_sdk_bedrock_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            aws_sdk_bedrock_agent.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            aws_sdk_bedrock_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agent.types.list_knowledge_base_documents_response.ListKnowledgeBaseDocumentsResponse"
        ]:
            import aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agent._operations.amazon_bedrock_agent_build_time_lambda.list_knowledge_base_documents.async_list_knowledge_base_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agent.types.list_knowledge_base_documents_request.ListKnowledgeBaseDocumentsRequest = {}  # type: ignore[typeddict-item]
        input_["knowledge_base_id"] = knowledge_base_id
        input_["data_source_id"] = data_source_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
