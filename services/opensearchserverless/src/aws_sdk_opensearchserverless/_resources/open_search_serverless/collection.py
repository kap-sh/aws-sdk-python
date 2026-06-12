from typing import TYPE_CHECKING, Optional

from aws_sdk_opensearchserverless._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.collection_filters
    import aws_sdk_opensearchserverless.types.collection_group_name
    import aws_sdk_opensearchserverless.types.collection_id
    import aws_sdk_opensearchserverless.types.collection_name
    import aws_sdk_opensearchserverless.types.collection_type
    import aws_sdk_opensearchserverless.types.create_collection_request
    import aws_sdk_opensearchserverless.types.create_collection_response
    import aws_sdk_opensearchserverless.types.delete_collection_request
    import aws_sdk_opensearchserverless.types.delete_collection_response
    import aws_sdk_opensearchserverless.types.deletion_protection
    import aws_sdk_opensearchserverless.types.encryption_config
    import aws_sdk_opensearchserverless.types.list_collections_request
    import aws_sdk_opensearchserverless.types.list_collections_response
    import aws_sdk_opensearchserverless.types.standby_replicas
    import aws_sdk_opensearchserverless.types.tags
    import aws_sdk_opensearchserverless.types.update_collection_request
    import aws_sdk_opensearchserverless.types.update_collection_response
    import aws_sdk_opensearchserverless.types.vector_options
    from aws_sdk_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from aws_sdk_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class Collection:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_opensearchserverless.types.collection_name.CollectionName",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        type: Optional[
            "aws_sdk_opensearchserverless.types.collection_type.CollectionType"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["aws_sdk_opensearchserverless.types.tags.Tags"] = None,
        standby_replicas: Optional[
            "aws_sdk_opensearchserverless.types.standby_replicas.StandbyReplicas"
        ] = None,
        vector_options: Optional[
            "aws_sdk_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        collection_group_name: Optional[
            "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
        ] = None,
        encryption_config: Optional[
            "aws_sdk_opensearchserverless.types.encryption_config.EncryptionConfig"
        ] = None,
        deletion_protection: Optional[
            "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_collection_response.CreateCollectionResponse":
        """<p>Creates a new OpenSearch Serverless collection. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            name: <p>Name of the collection.</p>
            type: <p>The type of collection.</p>
            description: <p>Description of the collection.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            collection_group_name: <p>The name of the collection group to associate with the collection.</p>
            encryption_config: <p>Encryption settings for the collection.</p>
            deletion_protection: <p>Indicates whether to enable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.create_collection_request.CreateCollectionRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.create_collection_response.CreateCollectionResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_collection

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.create_collection.create_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.create_collection_request.CreateCollectionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if type is not None:
            input["type"] = type
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if standby_replicas is not None:
            input["standby_replicas"] = standby_replicas
        if vector_options is not None:
            input["vector_options"] = vector_options
        if collection_group_name is not None:
            input["collection_group_name"] = collection_group_name
        if encryption_config is not None:
            input["encryption_config"] = encryption_config
        if deletion_protection is not None:
            input["deletion_protection"] = deletion_protection
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        id: "aws_sdk_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        vector_options: Optional[
            "aws_sdk_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        deletion_protection: Optional[
            "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_collection_response.UpdateCollectionResponse":
        """<p>Updates an OpenSearch Serverless collection.</p>

        Args:
            id: <p>The unique identifier of the collection.</p>
            description: <p>A description of the collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            deletion_protection: <p>Indicates whether to enable or disable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.update_collection_request.UpdateCollectionRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.update_collection_response.UpdateCollectionResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_collection

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.update_collection.update_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.update_collection_request.UpdateCollectionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if description is not None:
            input["description"] = description
        if vector_options is not None:
            input["vector_options"] = vector_options
        if deletion_protection is not None:
            input["deletion_protection"] = deletion_protection
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        id: "aws_sdk_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse":
        """<p>Deletes an OpenSearch Serverless collection. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection. For example, <code>1iu5usc406kd</code>. The ID is part of the collection endpoint. You can also retrieve it using the <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html\">ListCollections</a> API.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_collection

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.delete_collection.delete_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if client_token is not None:
            input["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        collection_filters: Optional[
            "aws_sdk_opensearchserverless.types.collection_filters.CollectionFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_collections_response.ListCollectionsResponse":
        """<p>Lists all OpenSearch Serverless collections. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p> <note> <p>Make sure to include an empty request body {} if you don't include any collection filters in the request.</p> </note>

        Args:
            collection_filters: <p> A list of filter names and values that you can use for requests.</p>
            next_token: <p>If your initial <code>ListCollections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollections</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.list_collections_request.ListCollectionsRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.list_collections_response.ListCollectionsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_collections

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.list_collections.list_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.list_collections_request.ListCollectionsRequest = {}  # type: ignore[typeddict-item]
        if collection_filters is not None:
            input["collection_filters"] = collection_filters
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncCollection:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_opensearchserverless.types.collection_name.CollectionName",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        type: Optional[
            "aws_sdk_opensearchserverless.types.collection_type.CollectionType"
        ] = None,
        description: Optional[str] = None,
        tags: Optional["aws_sdk_opensearchserverless.types.tags.Tags"] = None,
        standby_replicas: Optional[
            "aws_sdk_opensearchserverless.types.standby_replicas.StandbyReplicas"
        ] = None,
        vector_options: Optional[
            "aws_sdk_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        collection_group_name: Optional[
            "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName"
        ] = None,
        encryption_config: Optional[
            "aws_sdk_opensearchserverless.types.encryption_config.EncryptionConfig"
        ] = None,
        deletion_protection: Optional[
            "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_collection_response.CreateCollectionResponse":
        """<p>Creates a new OpenSearch Serverless collection. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            name: <p>Name of the collection.</p>
            type: <p>The type of collection.</p>
            description: <p>Description of the collection.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            collection_group_name: <p>The name of the collection group to associate with the collection.</p>
            encryption_config: <p>Encryption settings for the collection.</p>
            deletion_protection: <p>Indicates whether to enable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.create_collection_request.CreateCollectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.create_collection_response.CreateCollectionResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_collection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.create_collection.async_create_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.create_collection_request.CreateCollectionRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if type is not None:
            input["type"] = type
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if standby_replicas is not None:
            input["standby_replicas"] = standby_replicas
        if vector_options is not None:
            input["vector_options"] = vector_options
        if collection_group_name is not None:
            input["collection_group_name"] = collection_group_name
        if encryption_config is not None:
            input["encryption_config"] = encryption_config
        if deletion_protection is not None:
            input["deletion_protection"] = deletion_protection
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        id: "aws_sdk_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        vector_options: Optional[
            "aws_sdk_opensearchserverless.types.vector_options.VectorOptions"
        ] = None,
        deletion_protection: Optional[
            "aws_sdk_opensearchserverless.types.deletion_protection.DeletionProtection"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_collection_response.UpdateCollectionResponse":
        """<p>Updates an OpenSearch Serverless collection.</p>

        Args:
            id: <p>The unique identifier of the collection.</p>
            description: <p>A description of the collection.</p>
            vector_options: <p>Configuration options for vector search capabilities in the collection.</p>
            deletion_protection: <p>Indicates whether to enable or disable deletion protection for the collection. When set to <code>ENABLED</code>, the collection cannot be deleted.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.update_collection_request.UpdateCollectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.update_collection_response.UpdateCollectionResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_collection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.update_collection.async_update_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.update_collection_request.UpdateCollectionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if description is not None:
            input["description"] = description
        if vector_options is not None:
            input["vector_options"] = vector_options
        if deletion_protection is not None:
            input["deletion_protection"] = deletion_protection
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        id: "aws_sdk_opensearchserverless.types.collection_id.CollectionId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse":
        """<p>Deletes an OpenSearch Serverless collection. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection. For example, <code>1iu5usc406kd</code>. The ID is part of the collection endpoint. You can also retrieve it using the <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html\">ListCollections</a> API.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.delete_collection_response.DeleteCollectionResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_collection

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.delete_collection.async_delete_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.delete_collection_request.DeleteCollectionRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if client_token is not None:
            input["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        collection_filters: Optional[
            "aws_sdk_opensearchserverless.types.collection_filters.CollectionFilters"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_collections_response.ListCollectionsResponse":
        """<p>Lists all OpenSearch Serverless collections. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p> <note> <p>Make sure to include an empty request body {} if you don't include any collection filters in the request.</p> </note>

        Args:
            collection_filters: <p> A list of filter names and values that you can use for requests.</p>
            next_token: <p>If your initial <code>ListCollections</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollections</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.list_collections_request.ListCollectionsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.list_collections_response.ListCollectionsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_collections

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.list_collections.async_list_collections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.list_collections_request.ListCollectionsRequest = {}  # type: ignore[typeddict-item]
        if collection_filters is not None:
            input["collection_filters"] = collection_filters
        if next_token is not None:
            input["next_token"] = next_token
        if max_results is not None:
            input["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
