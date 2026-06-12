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
    import aws_sdk_opensearchserverless.types.collection_group_capacity_limits
    import aws_sdk_opensearchserverless.types.collection_group_id
    import aws_sdk_opensearchserverless.types.collection_group_name
    import aws_sdk_opensearchserverless.types.create_collection_group_request
    import aws_sdk_opensearchserverless.types.create_collection_group_response
    import aws_sdk_opensearchserverless.types.delete_collection_group_request
    import aws_sdk_opensearchserverless.types.delete_collection_group_response
    import aws_sdk_opensearchserverless.types.list_collection_groups_request
    import aws_sdk_opensearchserverless.types.list_collection_groups_response
    import aws_sdk_opensearchserverless.types.serverless_generation
    import aws_sdk_opensearchserverless.types.standby_replicas
    import aws_sdk_opensearchserverless.types.tags
    import aws_sdk_opensearchserverless.types.update_collection_group_request
    import aws_sdk_opensearchserverless.types.update_collection_group_response
    from aws_sdk_opensearchserverless._services.async_open_search_serverless import (
        AsyncOpenSearchServerlessClient,
        AsyncOpenSearchServerlessClientConfig,
    )
    from aws_sdk_opensearchserverless._services.open_search_serverless import (
        OpenSearchServerlessClient,
        OpenSearchServerlessClientConfig,
    )


class CollectionGroup:
    def __init__(self, service: OpenSearchServerlessClient) -> None:
        self._service = service

    def create(
        self,
        name: "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName",
        standby_replicas: "aws_sdk_opensearchserverless.types.standby_replicas.StandbyReplicas",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["aws_sdk_opensearchserverless.types.tags.Tags"] = None,
        capacity_limits: Optional[
            "aws_sdk_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        generation: Optional[
            "aws_sdk_opensearchserverless.types.serverless_generation.ServerlessGeneration"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse":
        """<p>Creates a collection group within OpenSearch Serverless. Collection groups let you manage OpenSearch Compute Units (OCUs) at a group level, with multiple collections sharing the group's capacity limits.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups.html\">Managing collection groups</a>.</p>

        Args:
            name: <p>The name of the collection group.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection group.</p>
            description: <p>A description of the collection group.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.</p>
            capacity_limits: <p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.</p>
            generation: <p>The generation of Amazon OpenSearch Serverless for the collection group. Valid values are <code>CLASSIC</code> and <code>NEXTGEN</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_collection_group

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.create_collection_group.create_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["standby_replicas"] = standby_replicas
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if capacity_limits is not None:
            input["capacity_limits"] = capacity_limits
        if generation is not None:
            input["generation"] = generation
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
        id: "aws_sdk_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        capacity_limits: Optional[
            "aws_sdk_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse":
        """<p>Updates the description and capacity limits of a collection group.</p>

        Args:
            id: <p>The unique identifier of the collection group to update.</p>
            description: <p>A new description for the collection group.</p>
            capacity_limits: <p>Updated capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_collection_group

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.update_collection_group.update_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if description is not None:
            input["description"] = description
        if capacity_limits is not None:
            input["capacity_limits"] = capacity_limits
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
        id: "aws_sdk_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[OpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse":
        """<p>Deletes a collection group. You can only delete empty collection groups that contain no collections. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection group to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_collection_group

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.delete_collection_group.delete_collection_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest = {}  # type: ignore[typeddict-item]
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
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse":
        """<p>Returns a list of collection groups. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            next_token: <p>If your initial <code>ListCollectionGroups</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollectionGroups</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_collection_groups

            output, http_response = (
                aws_sdk_opensearchserverless._operations.open_search_serverless.list_collection_groups.list_collection_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest = {}  # type: ignore[typeddict-item]
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


class AsyncCollectionGroup:
    def __init__(self, service: AsyncOpenSearchServerlessClient) -> None:
        self._service = service

    async def create(
        self,
        name: "aws_sdk_opensearchserverless.types.collection_group_name.CollectionGroupName",
        standby_replicas: "aws_sdk_opensearchserverless.types.standby_replicas.StandbyReplicas",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        tags: Optional["aws_sdk_opensearchserverless.types.tags.Tags"] = None,
        capacity_limits: Optional[
            "aws_sdk_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        generation: Optional[
            "aws_sdk_opensearchserverless.types.serverless_generation.ServerlessGeneration"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse":
        """<p>Creates a collection group within OpenSearch Serverless. Collection groups let you manage OpenSearch Compute Units (OCUs) at a group level, with multiple collections sharing the group's capacity limits.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collection-groups.html\">Managing collection groups</a>.</p>

        Args:
            name: <p>The name of the collection group.</p>
            standby_replicas: <p>Indicates whether standby replicas should be used for a collection group.</p>
            description: <p>A description of the collection group.</p>
            tags: <p>An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection group.</p>
            capacity_limits: <p>The capacity limits for the collection group, in OpenSearch Compute Units (OCUs). These limits control the maximum and minimum capacity for collections within the group.</p>
            generation: <p>The generation of Amazon OpenSearch Serverless for the collection group. Valid values are <code>CLASSIC</code> and <code>NEXTGEN</code>.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.create_collection_group_response.CreateCollectionGroupResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.create_collection_group

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.create_collection_group.async_create_collection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.create_collection_group_request.CreateCollectionGroupRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        input["standby_replicas"] = standby_replicas
        if description is not None:
            input["description"] = description
        if tags is not None:
            input["tags"] = tags
        if capacity_limits is not None:
            input["capacity_limits"] = capacity_limits
        if generation is not None:
            input["generation"] = generation
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
        id: "aws_sdk_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        description: Optional[str] = None,
        capacity_limits: Optional[
            "aws_sdk_opensearchserverless.types.collection_group_capacity_limits.CollectionGroupCapacityLimits"
        ] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse":
        """<p>Updates the description and capacity limits of a collection group.</p>

        Args:
            id: <p>The unique identifier of the collection group to update.</p>
            description: <p>A new description for the collection group.</p>
            capacity_limits: <p>Updated capacity limits for the collection group, in OpenSearch Compute Units (OCUs).</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.update_collection_group_response.UpdateCollectionGroupResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.update_collection_group

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.update_collection_group.async_update_collection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.update_collection_group_request.UpdateCollectionGroupRequest = {}  # type: ignore[typeddict-item]
        input["id"] = id
        if description is not None:
            input["description"] = description
        if capacity_limits is not None:
            input["capacity_limits"] = capacity_limits
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
        id: "aws_sdk_opensearchserverless.types.collection_group_id.CollectionGroupId",
        *,
        config_overrides: Optional[AsyncOpenSearchServerlessClientConfig] = None,
        client_token: Optional[
            "aws_sdk_opensearchserverless.types.client_token.ClientToken"
        ] = None,
    ) -> "aws_sdk_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse":
        """<p>Deletes a collection group. You can only delete empty collection groups that contain no collections. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            id: <p>The unique identifier of the collection group to delete.</p>
            client_token: <p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.delete_collection_group_response.DeleteCollectionGroupResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.delete_collection_group

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.delete_collection_group.async_delete_collection_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.delete_collection_group_request.DeleteCollectionGroupRequest = {}  # type: ignore[typeddict-item]
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
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "aws_sdk_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse":
        """<p>Returns a list of collection groups. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html\">Creating and managing Amazon OpenSearch Serverless collections</a>.</p>

        Args:
            next_token: <p>If your initial <code>ListCollectionGroups</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollectionGroups</code> operations, which returns results in the next page.</p>
            max_results: <p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_opensearchserverless.types.list_collection_groups_response.ListCollectionGroupsResponse"
        ]:
            import aws_sdk_opensearchserverless._operations.open_search_serverless.list_collection_groups

            (
                output,
                http_response,
            ) = await aws_sdk_opensearchserverless._operations.open_search_serverless.list_collection_groups.async_list_collection_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input: aws_sdk_opensearchserverless.types.list_collection_groups_request.ListCollectionGroupsRequest = {}  # type: ignore[typeddict-item]
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
