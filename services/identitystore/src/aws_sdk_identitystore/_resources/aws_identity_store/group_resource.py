from typing import TYPE_CHECKING, Optional

from aws_sdk_identitystore._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.attribute_operations
    import aws_sdk_identitystore.types.create_group_request
    import aws_sdk_identitystore.types.create_group_response
    import aws_sdk_identitystore.types.delete_group_request
    import aws_sdk_identitystore.types.delete_group_response
    import aws_sdk_identitystore.types.describe_group_request
    import aws_sdk_identitystore.types.describe_group_response
    import aws_sdk_identitystore.types.filters
    import aws_sdk_identitystore.types.group
    import aws_sdk_identitystore.types.group_display_name
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.list_groups_request
    import aws_sdk_identitystore.types.list_groups_response
    import aws_sdk_identitystore.types.max_results
    import aws_sdk_identitystore.types.next_token
    import aws_sdk_identitystore.types.resource_id
    import aws_sdk_identitystore.types.sensitive_string_type
    import aws_sdk_identitystore.types.update_group_request
    import aws_sdk_identitystore.types.update_group_response
    from aws_sdk_identitystore._services.async_identitystore import (
        AsyncidentitystoreClient,
        AsyncidentitystoreClientConfig,
    )
    from aws_sdk_identitystore._services.identitystore import (
        identitystoreClient,
        identitystoreClientConfig,
    )


class GroupResource:
    def __init__(self, service: identitystoreClient) -> None:
        self._service = service

    def create(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        display_name: Optional[
            "aws_sdk_identitystore.types.group_display_name.GroupDisplayName"
        ] = None,
        description: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
    ) -> "aws_sdk_identitystore.types.create_group_response.CreateGroupResponse":
        """<p>Creates a group within the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            display_name: <p>A string containing the name of the group. This value is commonly displayed when the group is referenced. <code>Administrator</code> and <code>AWSAdministrators</code> are reserved names and can't be used for users or groups.</p>
            description: <p>A string containing the description of the group.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.create_group_request.CreateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.create_group_response.CreateGroupResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.create_group

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.create_group.create_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.create_group_request.CreateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.describe_group_response.DescribeGroupResponse":
        """<p>Retrieves the group metadata and attributes from <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.describe_group_request.DescribeGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.describe_group_response.DescribeGroupResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.describe_group

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.describe_group.describe_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.describe_group_request.DescribeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        operations: "aws_sdk_identitystore.types.attribute_operations.AttributeOperations",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.update_group_response.UpdateGroupResponse":
        """<p>Updates the specified group metadata and attributes in the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            operations: <p>A list of <code>AttributeOperation</code> objects to apply to the requested group. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html\">Group</a>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.update_group_request.UpdateGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.update_group_response.UpdateGroupResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.update_group

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.update_group.update_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.update_group_request.UpdateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id
        input_["operations"] = operations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.delete_group_response.DeleteGroupResponse":
        """<p>Delete a group within an identity store given <code>GroupId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.delete_group_request.DeleteGroupRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.delete_group_response.DeleteGroupResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.delete_group

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.delete_group.delete_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.delete_group_request.DeleteGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_identitystore.types.filters.Filters"] = None,
    ) -> "aws_sdk_identitystore.types.list_groups_response.ListGroupsResponse":
        """<p>Lists all groups in the identity store. Returns a paginated list of complete <code>Group</code> objects. Filtering for a <code>Group</code> by the <code>DisplayName</code> attribute is deprecated. Instead, use the <code>GetGroupId</code> API action.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in the <code> ListUsers</code> and <code>ListGroups</code> requests to specify how many results to return in one page. The length limit is 50 characters.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code> and <code>ListGroups</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>
            filters: <p>A list of <code>Filter</code> objects, which is used in the <code>ListUsers</code> and <code> ListGroups</code> requests.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.list_groups_request.ListGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.list_groups_response.ListGroupsResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.list_groups

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.list_groups.list_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.list_groups_request.ListGroupsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncGroupResource:
    def __init__(self, service: AsyncidentitystoreClient) -> None:
        self._service = service

    async def create(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        display_name: Optional[
            "aws_sdk_identitystore.types.group_display_name.GroupDisplayName"
        ] = None,
        description: Optional[
            "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
        ] = None,
    ) -> "aws_sdk_identitystore.types.create_group_response.CreateGroupResponse":
        """<p>Creates a group within the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            display_name: <p>A string containing the name of the group. This value is commonly displayed when the group is referenced. <code>Administrator</code> and <code>AWSAdministrators</code> are reserved names and can't be used for users or groups.</p>
            description: <p>A string containing the description of the group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.create_group_request.CreateGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.create_group_response.CreateGroupResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.create_group

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.create_group.async_create_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.create_group_request.CreateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.describe_group_response.DescribeGroupResponse":
        """<p>Retrieves the group metadata and attributes from <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.describe_group_request.DescribeGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.describe_group_response.DescribeGroupResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.describe_group

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.describe_group.async_describe_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.describe_group_request.DescribeGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        operations: "aws_sdk_identitystore.types.attribute_operations.AttributeOperations",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.update_group_response.UpdateGroupResponse":
        """<p>Updates the specified group metadata and attributes in the specified identity store.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            operations: <p>A list of <code>AttributeOperation</code> objects to apply to the requested group. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html\">Group</a>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.update_group_request.UpdateGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.update_group_response.UpdateGroupResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.update_group

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.update_group.async_update_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.update_group_request.UpdateGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id
        input_["operations"] = operations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.delete_group_response.DeleteGroupResponse":
        """<p>Delete a group within an identity store given <code>GroupId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.delete_group_request.DeleteGroupRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.delete_group_response.DeleteGroupResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.delete_group

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.delete_group.async_delete_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.delete_group_request.DeleteGroupRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
        filters: Optional["aws_sdk_identitystore.types.filters.Filters"] = None,
    ) -> "aws_sdk_identitystore.types.list_groups_response.ListGroupsResponse":
        """<p>Lists all groups in the identity store. Returns a paginated list of complete <code>Group</code> objects. Filtering for a <code>Group</code> by the <code>DisplayName</code> attribute is deprecated. Instead, use the <code>GetGroupId</code> API action.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store, such as <code>d-1234567890</code>. In this example, <code>d-</code> is a fixed prefix, and <code>1234567890</code> is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in the <code> ListUsers</code> and <code>ListGroups</code> requests to specify how many results to return in one page. The length limit is 50 characters.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code> and <code>ListGroups</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>
            filters: <p>A list of <code>Filter</code> objects, which is used in the <code>ListUsers</code> and <code> ListGroups</code> requests.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.list_groups_request.ListGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.list_groups_response.ListGroupsResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.list_groups

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.list_groups.async_list_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.list_groups_request.ListGroupsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
