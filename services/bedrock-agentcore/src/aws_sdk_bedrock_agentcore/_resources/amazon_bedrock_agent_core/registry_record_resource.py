from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import aws_sdk_bedrock_agentcore._auth._signers
import aws_sdk_bedrock_agentcore._auth._sigv4
from aws_sdk_bedrock_agentcore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.metadata_filter_expression
    import aws_sdk_bedrock_agentcore.types.registry_id_list
    import aws_sdk_bedrock_agentcore.types.search_registry_records_request
    import aws_sdk_bedrock_agentcore.types.search_registry_records_response
    from aws_sdk_bedrock_agentcore._services.async_bedrock_agent_core import (
        AsyncBedrockAgentCoreClient,
        AsyncBedrockAgentCoreClientConfig,
    )
    from aws_sdk_bedrock_agentcore._services.bedrock_agent_core import (
        BedrockAgentCoreClient,
        BedrockAgentCoreClientConfig,
    )


class RegistryRecordResource:
    def __init__(self, service: BedrockAgentCoreClient) -> None:
        self._service = service

    def search_registry_records(
        self,
        search_query: str,
        registry_ids: "aws_sdk_bedrock_agentcore.types.registry_id_list.RegistryIdList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "aws_sdk_bedrock_agentcore.types.metadata_filter_expression.MetadataFilterExpression"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse":
        r"""<p> Searches for registry records using semantic, lexical, or hybrid queries. Returns metadata for matching records ordered by relevance within the specified registry.</p>

        Args:
            search_query: <p> The search query to find matching registry records.</p>
            registry_ids: <p> The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the 12-character alphanumeric registry ID.</p>
            max_results: <p> The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.</p>
            filters: <p> A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (<code>$eq</code>, <code>$ne</code>, <code>$in</code>) and logical operators (<code>$and</code>, <code>$or</code>) on filterable fields (<code>name</code>, <code>descriptorType</code>, <code>version</code>). For example, to filter by descriptor type: <code>{\"descriptorType\": {\"$eq\": \"MCP\"}}</code>. To combine filters: <code>{\"$and\": [{\"descriptorType\": {\"$eq\": \"MCP\"}}, {\"name\": {\"$eq\": \"my-tool\"}}]}</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest]",
        ) -> OperationResponse[
            "aws_sdk_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records

            output, http_response = (
                aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records.search_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest = {}  # type: ignore[typeddict-item]
        input_["search_query"] = search_query
        input_["registry_ids"] = registry_ids
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncRegistryRecordResource:
    def __init__(self, service: AsyncBedrockAgentCoreClient) -> None:
        self._service = service

    async def search_registry_records(
        self,
        search_query: str,
        registry_ids: "aws_sdk_bedrock_agentcore.types.registry_id_list.RegistryIdList",
        *,
        config_overrides: Optional[AsyncBedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "aws_sdk_bedrock_agentcore.types.metadata_filter_expression.MetadataFilterExpression"
        ] = None,
    ) -> "aws_sdk_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse":
        r"""<p> Searches for registry records using semantic, lexical, or hybrid queries. Returns metadata for matching records ordered by relevance within the specified registry.</p>

        Args:
            search_query: <p> The search query to find matching registry records.</p>
            registry_ids: <p> The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the 12-character alphanumeric registry ID.</p>
            max_results: <p> The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.</p>
            filters: <p> A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (<code>$eq</code>, <code>$ne</code>, <code>$in</code>) and logical operators (<code>$and</code>, <code>$or</code>) on filterable fields (<code>name</code>, <code>descriptorType</code>, <code>version</code>). For example, to filter by descriptor type: <code>{\"descriptorType\": {\"$eq\": \"MCP\"}}</code>. To combine filters: <code>{\"$and\": [{\"descriptorType\": {\"$eq\": \"MCP\"}}, {\"name\": {\"$eq\": \"my-tool\"}}]}</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse"
        ]:
            import aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records

            (
                output,
                http_response,
            ) = await aws_sdk_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records.async_search_registry_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest = {}  # type: ignore[typeddict-item]
        input_["search_query"] = search_query
        input_["registry_ids"] = registry_ids
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
