"""Generated from Smithy shape ``com.amazonaws.notifications#Notifications``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_notifications._auth._signers
import aws_sdk_notifications._auth._sigv4
from aws_sdk_notifications._auth._identity import Credentials
from aws_sdk_notifications._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_notifications._auth._zapros_handler import AuthMiddleware
from aws_sdk_notifications._pagination import resolve_path as _resolve_path
from aws_sdk_notifications._resources.notifications.channel import AsyncChannel
from aws_sdk_notifications._resources.notifications.event_rule import AsyncEventRule
from aws_sdk_notifications._resources.notifications.managed_notification_account_contact_association import (
    AsyncManagedNotificationAccountContactAssociation,
)
from aws_sdk_notifications._resources.notifications.managed_notification_additional_channel_association import (
    AsyncManagedNotificationAdditionalChannelAssociation,
)
from aws_sdk_notifications._resources.notifications.managed_notification_child_event_resource import (
    AsyncManagedNotificationChildEventResource,
)
from aws_sdk_notifications._resources.notifications.managed_notification_configuration import (
    AsyncManagedNotificationConfiguration,
)
from aws_sdk_notifications._resources.notifications.managed_notification_event_resource import (
    AsyncManagedNotificationEventResource,
)
from aws_sdk_notifications._resources.notifications.notification_configuration import (
    AsyncNotificationConfiguration,
)
from aws_sdk_notifications._resources.notifications.notification_event_resource import (
    AsyncNotificationEventResource,
)
from aws_sdk_notifications._resources.notifications.notification_hub import (
    AsyncNotificationHub,
)
from aws_sdk_notifications._resources.notifications.organization_access import (
    AsyncOrganizationAccess,
)
from aws_sdk_notifications._resources.notifications.organizational_unit import (
    AsyncOrganizationalUnit,
)
from aws_sdk_notifications._services._aws_config import aaws_config
from aws_sdk_notifications._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_notifications.types.account_id
    import aws_sdk_notifications.types.list_managed_notification_channel_associations_request
    import aws_sdk_notifications.types.list_managed_notification_channel_associations_response
    import aws_sdk_notifications.types.list_member_accounts_request
    import aws_sdk_notifications.types.list_member_accounts_response
    import aws_sdk_notifications.types.list_tags_for_resource_request
    import aws_sdk_notifications.types.list_tags_for_resource_response
    import aws_sdk_notifications.types.managed_notification_channel_association_summary
    import aws_sdk_notifications.types.managed_notification_configuration_os_arn
    import aws_sdk_notifications.types.member_account
    import aws_sdk_notifications.types.member_account_notification_configuration_status
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.organizational_unit_id
    import aws_sdk_notifications.types.tag_keys
    import aws_sdk_notifications.types.tag_map
    import aws_sdk_notifications.types.tag_resource_request
    import aws_sdk_notifications.types.tag_resource_response
    import aws_sdk_notifications.types.untag_resource_request
    import aws_sdk_notifications.types.untag_resource_response


class AsyncNotificationsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncNotificationsClient:
    """A client for the ``Notifications`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncNotificationsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.channel = AsyncChannel(self)
        self.event_rule = AsyncEventRule(self)
        self.managed_notification_account_contact_association = (
            AsyncManagedNotificationAccountContactAssociation(self)
        )
        self.managed_notification_additional_channel_association = (
            AsyncManagedNotificationAdditionalChannelAssociation(self)
        )
        self.managed_notification_child_event_resource = (
            AsyncManagedNotificationChildEventResource(self)
        )
        self.managed_notification_configuration = AsyncManagedNotificationConfiguration(
            self
        )
        self.managed_notification_event_resource = (
            AsyncManagedNotificationEventResource(self)
        )
        self.notification_configuration = AsyncNotificationConfiguration(self)
        self.notification_event_resource = AsyncNotificationEventResource(self)
        self.notification_hub = AsyncNotificationHub(self)
        self.organization_access = AsyncOrganizationAccess(self)
        self.organizational_unit = AsyncOrganizationalUnit(self)

    def operation_options(
        self, config_overrides: Optional[AsyncNotificationsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncNotificationsClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def list_managed_notification_channel_associations(
        self,
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_notifications.types.list_managed_notification_channel_associations_response.ListManagedNotificationChannelAssociationsResponse":
        """<p>Returns a list of Account contacts and Channels associated with a <code>ManagedNotificationConfiguration</code>, in paginated format.</p>

        Args:
            managed_notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code> to match.</p>
            max_results: <p>The maximum number of results to be returned in this call. Defaults to 20.</p>
            next_token: <p>The start token for paginated calls. Retrieved from the response of a previous <code>ListManagedNotificationChannelAssociations</code> call.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_managed_notification_channel_associations_request.ListManagedNotificationChannelAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_managed_notification_channel_associations_response.ListManagedNotificationChannelAssociationsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_managed_notification_channel_associations

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_managed_notification_channel_associations.async_list_managed_notification_channel_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_managed_notification_channel_associations_request.ListManagedNotificationChannelAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["managed_notification_configuration_arn"] = (
            managed_notification_configuration_arn
        )
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

    async def iter_list_managed_notification_channel_associations(
        self,
        managed_notification_configuration_arn: "aws_sdk_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[aws_sdk_notifications.types.managed_notification_channel_association_summary.ManagedNotificationChannelAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_managed_notification_channel_associations(
                managed_notification_configuration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channel_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_member_accounts(
        self,
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
        member_account: Optional[
            "aws_sdk_notifications.types.account_id.AccountId"
        ] = None,
        status: Optional[
            "aws_sdk_notifications.types.member_account_notification_configuration_status.MemberAccountNotificationConfigurationStatus"
        ] = None,
        organizational_unit_id: Optional[
            "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
    ) -> "aws_sdk_notifications.types.list_member_accounts_response.ListMemberAccountsResponse":
        """<p>Returns a list of member accounts associated with a notification configuration.</p>

        Args:
            notification_configuration_arn: <p>The Amazon Resource Name (ARN) of the notification configuration used to filter the member accounts.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid values are 1-100.</p>
            next_token: <p>The token for the next page of results. Use the value returned in the previous response.</p>
            member_account: <p>The member account identifier used to filter the results.</p>
            status: <p>The status used to filter the member accounts.</p>
            organizational_unit_id: <p>The organizational unit ID used to filter the member accounts.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_member_accounts_request.ListMemberAccountsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_member_accounts_response.ListMemberAccountsResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_member_accounts

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_member_accounts.async_list_member_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_member_accounts_request.ListMemberAccountsRequest = {}  # type: ignore[typeddict-item]
        input_["notification_configuration_arn"] = notification_configuration_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if member_account is not None:
            input_["member_account"] = member_account
        if status is not None:
            input_["status"] = status
        if organizational_unit_id is not None:
            input_["organizational_unit_id"] = organizational_unit_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_member_accounts(
        self,
        notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_notifications.types.next_token.NextToken"] = None,
        member_account: Optional[
            "aws_sdk_notifications.types.account_id.AccountId"
        ] = None,
        status: Optional[
            "aws_sdk_notifications.types.member_account_notification_configuration_status.MemberAccountNotificationConfigurationStatus"
        ] = None,
        organizational_unit_id: Optional[
            "aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_notifications.types.member_account.MemberAccount]":
        _token = next_token
        while True:
            _response = await self.list_member_accounts(
                notification_configuration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                member_account=member_account,
                status=status,
                organizational_unit_id=organizational_unit_id,
            )
            _page = _resolve_path(_response, ("member_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>Returns a list of tags for a specified Amazon Resource Name (ARN).</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html\">Tagging your Amazon Web Services resources</a> in the <i>Tagging Amazon Web Services Resources User Guide</i>.</p> <note> <p>This is only supported for <code>NotificationConfigurations</code>.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to list tags.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        tags: "aws_sdk_notifications.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.tag_resource_response.TagResourceResponse":
        r"""<p>Tags the resource with a tag key and value.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html\">Tagging your Amazon Web Services resources</a> in the <i>Tagging Amazon Web Services Resources User Guide</i>.</p> <note> <p>This is only supported for <code>NotificationConfigurations</code>.</p> </note>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to tag a resource.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn",
        tag_keys: "aws_sdk_notifications.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncNotificationsClientConfig] = None,
    ) -> "aws_sdk_notifications.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Untags a resource with a specified Amazon Resource Name (ARN).</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html\">Tagging your Amazon Web Services resources</a> in the <i>Tagging Amazon Web Services Resources User Guide</i>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) to use to untag a resource.</p>
            tag_keys: <p>The tag keys to use to untag a resource.</p>

        Raises:
            aws_sdk_notifications.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            aws_sdk_notifications.errors.internal_server_exception.InternalServerException: <p>Unexpected error during processing of request.</p>
            aws_sdk_notifications.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist. </p>
            aws_sdk_notifications.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling. </p>
            aws_sdk_notifications.errors.validation_exception.ValidationException: <p>This exception is thrown when the notification event fails validation.</p>
            aws_sdk_notifications.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_notifications.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_notifications.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_notifications._operations.notifications.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_notifications._operations.notifications.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_notifications.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["arn"] = arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
