from __future__ import annotations

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
    import aws_sdk_identitystore.types.create_group_membership_request
    import aws_sdk_identitystore.types.create_group_membership_response
    import aws_sdk_identitystore.types.delete_group_membership_request
    import aws_sdk_identitystore.types.delete_group_membership_response
    import aws_sdk_identitystore.types.describe_group_membership_request
    import aws_sdk_identitystore.types.describe_group_membership_response
    import aws_sdk_identitystore.types.group_membership
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.list_group_memberships_request
    import aws_sdk_identitystore.types.list_group_memberships_response
    import aws_sdk_identitystore.types.max_results
    import aws_sdk_identitystore.types.member_id
    import aws_sdk_identitystore.types.next_token
    import aws_sdk_identitystore.types.resource_id
    from aws_sdk_identitystore._services.async_identitystore import (
        AsyncidentitystoreClient,
        AsyncidentitystoreClientConfig,
    )
    from aws_sdk_identitystore._services.identitystore import (
        identitystoreClient,
        identitystoreClientConfig,
    )


class GroupMembershipResource:
    def __init__(self, service: identitystoreClient) -> None:
        self._service = service

    def create(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse":
        """<p>Creates a relationship between a member and a group. The following identifiers must be specified: <code>GroupId</code>, <code>IdentityStoreId</code>, and <code>MemberId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.create_group_membership_request.CreateGroupMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.create_group_membership

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.create_group_membership.create_group_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.create_group_membership_request.CreateGroupMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id
        input_["member_id"] = member_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse":
        r"""<p>Retrieves membership metadata and attributes from <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.describe_group_membership_request.DescribeGroupMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.describe_group_membership

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.describe_group_membership.describe_group_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.describe_group_membership_request.DescribeGroupMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["membership_id"] = membership_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse":
        """<p>Delete a membership within a group given <code>MembershipId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.delete_group_membership_request.DeleteGroupMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.delete_group_membership

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.delete_group_membership.delete_group_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.delete_group_membership_request.DeleteGroupMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["membership_id"] = membership_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse":
        r"""<p>For the specified group in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code> List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code> and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.list_group_memberships_request.ListGroupMembershipsRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.list_group_memberships

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.list_group_memberships.list_group_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.list_group_memberships_request.ListGroupMembershipsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id
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


class AsyncGroupMembershipResource:
    def __init__(self, service: AsyncidentitystoreClient) -> None:
        self._service = service

    async def create(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse":
        """<p>Creates a relationship between a member and a group. The following identifiers must be specified: <code>GroupId</code>, <code>IdentityStoreId</code>, and <code>MemberId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the number of users or groups in the identity store to exceed the maximum allowed.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.create_group_membership_request.CreateGroupMembershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.create_group_membership_response.CreateGroupMembershipResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.create_group_membership

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.create_group_membership.async_create_group_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.create_group_membership_request.CreateGroupMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id
        input_["member_id"] = member_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse":
        r"""<p>Retrieves membership metadata and attributes from <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.describe_group_membership_request.DescribeGroupMembershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.describe_group_membership_response.DescribeGroupMembershipResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.describe_group_membership

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.describe_group_membership.async_describe_group_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.describe_group_membership_request.DescribeGroupMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["membership_id"] = membership_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        membership_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse":
        """<p>Delete a membership within a group given <code>MembershipId</code>.</p>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            membership_id: <p>The identifier for a <code>GroupMembership</code> in an identity store.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.conflict_exception.ConflictException: <p>This request cannot be completed for one of the following reasons:</p> <ul> <li> <p>Performing the requested operation would violate an existing uniqueness claim in the identity store. Resolve the conflict before retrying this request.</p> </li> <li> <p>The requested resource was being concurrently modified by another request.</p> </li> </ul>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.delete_group_membership_request.DeleteGroupMembershipRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.delete_group_membership_response.DeleteGroupMembershipResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.delete_group_membership

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.delete_group_membership.async_delete_group_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.delete_group_membership_request.DeleteGroupMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["membership_id"] = membership_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse":
        r"""<p>For the specified group in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in all <code> List</code> requests to specify how many results to return in one page.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code> and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.list_group_memberships_request.ListGroupMembershipsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.list_group_memberships_response.ListGroupMembershipsResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.list_group_memberships

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.list_group_memberships.async_list_group_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.list_group_memberships_request.ListGroupMembershipsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id
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
