"""Generated from Smithy shape ``com.amazonaws.identitystore#AWSIdentityStore``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_identitystore._auth._signers
import aws_sdk_identitystore._auth._sigv4
from aws_sdk_identitystore._auth._identity import Credentials
from aws_sdk_identitystore._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_identitystore._auth._zapros_handler import AuthMiddleware
from aws_sdk_identitystore._pagination import resolve_path as _resolve_path
from aws_sdk_identitystore._resources.aws_identity_store.group_membership_resource import (
    GroupMembershipResource,
)
from aws_sdk_identitystore._resources.aws_identity_store.group_resource import (
    GroupResource,
)
from aws_sdk_identitystore._resources.aws_identity_store.user_resource import (
    UserResource,
)
from aws_sdk_identitystore._services._aws_config import aws_config
from aws_sdk_identitystore._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.alternate_identifier
    import aws_sdk_identitystore.types.get_group_id_request
    import aws_sdk_identitystore.types.get_group_id_response
    import aws_sdk_identitystore.types.get_group_membership_id_request
    import aws_sdk_identitystore.types.get_group_membership_id_response
    import aws_sdk_identitystore.types.get_user_id_request
    import aws_sdk_identitystore.types.get_user_id_response
    import aws_sdk_identitystore.types.group_ids
    import aws_sdk_identitystore.types.group_membership
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.is_member_in_groups_request
    import aws_sdk_identitystore.types.is_member_in_groups_response
    import aws_sdk_identitystore.types.list_group_memberships_for_member_request
    import aws_sdk_identitystore.types.list_group_memberships_for_member_response
    import aws_sdk_identitystore.types.max_results
    import aws_sdk_identitystore.types.member_id
    import aws_sdk_identitystore.types.next_token
    import aws_sdk_identitystore.types.resource_id


class identitystoreClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class identitystoreClient:
    """A client for the ``identitystore`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = identitystoreClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.group_membership_resource = GroupMembershipResource(self)
        self.group_resource = GroupResource(self)
        self.user_resource = UserResource(self)

    def operation_options(
        self, config_overrides: Optional[identitystoreClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: identitystoreClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def get_group_id(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        alternate_identifier: "aws_sdk_identitystore.types.alternate_identifier.AlternateIdentifier",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.get_group_id_response.GetGroupIdResponse":
        r"""<p>Retrieves <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            alternate_identifier: <p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid path is <code> displayName</code>.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.get_group_id_request.GetGroupIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.get_group_id_response.GetGroupIdResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.get_group_id

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.get_group_id.get_group_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.get_group_id_request.GetGroupIdRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["alternate_identifier"] = alternate_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_group_membership_id(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse":
        r"""<p>Retrieves the <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.get_group_membership_id_request.GetGroupMembershipIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.get_group_membership_id

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.get_group_membership_id.get_group_membership_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.get_group_membership_id_request.GetGroupMembershipIdRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id
        input_["member_id"] = member_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_user_id(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        alternate_identifier: "aws_sdk_identitystore.types.alternate_identifier.AlternateIdentifier",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.get_user_id_response.GetUserIdResponse":
        r"""<p>Retrieves the <code>UserId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            alternate_identifier: <p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid paths are <code> userName</code> and <code>emails.value</code>.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.get_user_id_request.GetUserIdRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.get_user_id_response.GetUserIdResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.get_user_id

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.get_user_id.get_user_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.get_user_id_request.GetUserIdRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["alternate_identifier"] = alternate_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def is_member_in_groups(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        group_ids: "aws_sdk_identitystore.types.group_ids.GroupIds",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.is_member_in_groups_response.IsMemberInGroupsResponse":
        r"""<p>Checks the user's membership in all requested groups and returns if the member exists in all queried groups.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            member_id: <p>An object containing the identifier of a group member.</p>
            group_ids: <p>A list of identifiers for groups in the identity store.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.is_member_in_groups_request.IsMemberInGroupsRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.is_member_in_groups_response.IsMemberInGroupsResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.is_member_in_groups

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.is_member_in_groups.is_member_in_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.is_member_in_groups_request.IsMemberInGroupsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["member_id"] = member_id
        input_["group_ids"] = group_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_group_memberships_for_member(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_identitystore.types.list_group_memberships_for_member_response.ListGroupMembershipsForMemberResponse":
        r"""<p>For the specified member in the specified identity store, returns the list of all <code> GroupMembership</code> objects and returns results in paginated form.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>
            max_results: <p>The maximum number of results to be returned per request. This parameter is used in the <code> ListUsers</code> and <code>ListGroups</code> requests to specify how many results to return in one page. The length limit is 50 characters.</p>
            next_token: <p>The pagination token used for the <code>ListUsers</code>, <code>ListGroups</code>, and <code> ListGroupMemberships</code> API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.</p>

        Raises:
            aws_sdk_identitystore.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            aws_sdk_identitystore.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure with an internal server.</p>
            aws_sdk_identitystore.errors.throttling_exception.ThrottlingException: <p>Indicates that the principal has crossed the throttling limits of the API operations.</p>
            aws_sdk_identitystore.errors.resource_not_found_exception.ResourceNotFoundException: <p>Indicates that a requested resource is not found.</p>
            aws_sdk_identitystore.errors.validation_exception.ValidationException: <p>The request failed because it contains a syntax error.</p>
            aws_sdk_identitystore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[aws_sdk_identitystore.types.list_group_memberships_for_member_request.ListGroupMembershipsForMemberRequest]",
        ) -> OperationResponse[
            "aws_sdk_identitystore.types.list_group_memberships_for_member_response.ListGroupMembershipsForMemberResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.list_group_memberships_for_member

            output, http_response = (
                aws_sdk_identitystore._operations.aws_identity_store.list_group_memberships_for_member.list_group_memberships_for_member(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.list_group_memberships_for_member_request.ListGroupMembershipsForMemberRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["member_id"] = member_id
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

    def iter_list_group_memberships_for_member(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[identitystoreClientConfig] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
    ) -> "Iterator[aws_sdk_identitystore.types.group_membership.GroupMembership]":
        _token = next_token
        while True:
            _response = self.list_group_memberships_for_member(
                identity_store_id,
                member_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("group_memberships",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
