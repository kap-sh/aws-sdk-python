"""Generated from Smithy shape ``com.amazonaws.identitystore#AWSIdentityStore``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_identitystore._auth._signers
import aws_sdk_identitystore._auth._sigv4
from aws_sdk_identitystore._auth._identity import Credentials
from aws_sdk_identitystore._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_identitystore._auth._zapros_handler import AuthMiddleware
from aws_sdk_identitystore._pagination import resolve_path as _resolve_path
from aws_sdk_identitystore._resources.aws_identity_store.group_membership_resource import (
    AsyncGroupMembershipResource,
)
from aws_sdk_identitystore._resources.aws_identity_store.group_resource import (
    AsyncGroupResource,
)
from aws_sdk_identitystore._resources.aws_identity_store.user_resource import (
    AsyncUserResource,
)
from aws_sdk_identitystore._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
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


class AsyncidentitystoreClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


async def ensure_async_iterator(
    it: AsyncIterator[bytes] | bytes,
) -> AsyncIterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        async for chunk in it:
            yield chunk


class AsyncidentitystoreClient:
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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = AsyncidentitystoreClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": DEFAULT_RETRY_MAX_ATTEMPTS
                if retry_max_attempts is None
                else retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": credentials_provider,
            }
        )

        # resources
        self.group_membership_resource = AsyncGroupMembershipResource(self)
        self.group_resource = AsyncGroupResource(self)
        self.user_resource = AsyncUserResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncidentitystoreClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncidentitystoreClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self._config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
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

    async def get_group_id(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        alternate_identifier: "aws_sdk_identitystore.types.alternate_identifier.AlternateIdentifier",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.get_group_id_response.GetGroupIdResponse":
        r"""<p>Retrieves <code>GroupId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            alternate_identifier: <p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid path is <code> displayName</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.get_group_id_request.GetGroupIdRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.get_group_id_response.GetGroupIdResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.get_group_id

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.get_group_id.async_get_group_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.get_group_id_request.GetGroupIdRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["alternate_identifier"] = alternate_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_group_membership_id(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        group_id: "aws_sdk_identitystore.types.resource_id.ResourceId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse":
        r"""<p>Retrieves the <code>MembershipId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            group_id: <p>The identifier for a group in the identity store.</p>
            member_id: <p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.get_group_membership_id_request.GetGroupMembershipIdRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.get_group_membership_id_response.GetGroupMembershipIdResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.get_group_membership_id

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.get_group_membership_id.async_get_group_membership_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.get_group_membership_id_request.GetGroupMembershipIdRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["group_id"] = group_id
        input_["member_id"] = member_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_user_id(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        alternate_identifier: "aws_sdk_identitystore.types.alternate_identifier.AlternateIdentifier",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.get_user_id_response.GetUserIdResponse":
        r"""<p>Retrieves the <code>UserId</code> in an identity store.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            alternate_identifier: <p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid paths are <code> userName</code> and <code>emails.value</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.get_user_id_request.GetUserIdRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.get_user_id_response.GetUserIdResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.get_user_id

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.get_user_id.async_get_user_id(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.get_user_id_request.GetUserIdRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["alternate_identifier"] = alternate_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def is_member_in_groups(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        group_ids: "aws_sdk_identitystore.types.group_ids.GroupIds",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
    ) -> "aws_sdk_identitystore.types.is_member_in_groups_response.IsMemberInGroupsResponse":
        r"""<p>Checks the user's membership in all requested groups and returns if the member exists in all queried groups.</p> <note> <p>If you have access to a member account, you can use this API operation from the member account. For more information, see <a href=\"https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html#limiting-access-from-member-accounts\">Limiting access to the identity store from member accounts</a> in the <i> IAM Identity Center User Guide</i>.</p> </note>

        Args:
            identity_store_id: <p>The globally unique identifier for the identity store.</p>
            member_id: <p>An object containing the identifier of a group member.</p>
            group_ids: <p>A list of identifiers for groups in the identity store.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.is_member_in_groups_request.IsMemberInGroupsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.is_member_in_groups_response.IsMemberInGroupsResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.is_member_in_groups

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.is_member_in_groups.async_is_member_in_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.is_member_in_groups_request.IsMemberInGroupsRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["member_id"] = member_id
        input_["group_ids"] = group_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_group_memberships_for_member(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
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
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_identitystore.types.list_group_memberships_for_member_request.ListGroupMembershipsForMemberRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_identitystore.types.list_group_memberships_for_member_response.ListGroupMembershipsForMemberResponse"
        ]:
            import aws_sdk_identitystore._operations.aws_identity_store.list_group_memberships_for_member

            (
                output,
                http_response,
            ) = await aws_sdk_identitystore._operations.aws_identity_store.list_group_memberships_for_member.async_list_group_memberships_for_member(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_identitystore.types.list_group_memberships_for_member_request.ListGroupMembershipsForMemberRequest = {}  # type: ignore[typeddict-item]
        input_["identity_store_id"] = identity_store_id
        input_["member_id"] = member_id
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

    async def iter_list_group_memberships_for_member(
        self,
        identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId",
        member_id: "aws_sdk_identitystore.types.member_id.MemberId",
        *,
        config_overrides: Optional[AsyncidentitystoreClientConfig] = None,
        max_results: Optional[
            "aws_sdk_identitystore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["aws_sdk_identitystore.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_identitystore.types.group_membership.GroupMembership]":
        _token = next_token
        while True:
            _response = await self.list_group_memberships_for_member(
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
