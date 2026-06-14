"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#RolesAnywhere``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_rolesanywhere._auth._signers
import aws_sdk_rolesanywhere._auth._sigv4
from aws_sdk_rolesanywhere._auth._identity import Credentials
from aws_sdk_rolesanywhere._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_rolesanywhere._auth._zapros_handler import AuthMiddleware
from aws_sdk_rolesanywhere._resources.roles_anywhere.crl import AsyncCrl
from aws_sdk_rolesanywhere._resources.roles_anywhere.profile import AsyncProfile
from aws_sdk_rolesanywhere._resources.roles_anywhere.subject import AsyncSubject
from aws_sdk_rolesanywhere._resources.roles_anywhere.trust_anchor import (
    AsyncTrustAnchor,
)
from aws_sdk_rolesanywhere._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_rolesanywhere.types.amazon_resource_name
    import aws_sdk_rolesanywhere.types.list_tags_for_resource_request
    import aws_sdk_rolesanywhere.types.list_tags_for_resource_response
    import aws_sdk_rolesanywhere.types.notification_setting_keys
    import aws_sdk_rolesanywhere.types.notification_settings
    import aws_sdk_rolesanywhere.types.put_notification_settings_request
    import aws_sdk_rolesanywhere.types.put_notification_settings_response
    import aws_sdk_rolesanywhere.types.reset_notification_settings_request
    import aws_sdk_rolesanywhere.types.reset_notification_settings_response
    import aws_sdk_rolesanywhere.types.tag_key_list
    import aws_sdk_rolesanywhere.types.tag_list
    import aws_sdk_rolesanywhere.types.tag_resource_request
    import aws_sdk_rolesanywhere.types.tag_resource_response
    import aws_sdk_rolesanywhere.types.untag_resource_request
    import aws_sdk_rolesanywhere.types.untag_resource_response
    import aws_sdk_rolesanywhere.types.uuid


class AsyncRolesAnywhereClientConfig(TypedDict, total=False):
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


class AsyncRolesAnywhereClient:
    """A client for the ``RolesAnywhere`` service.

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
        self.config = AsyncRolesAnywhereClientConfig(
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
        self.crl = AsyncCrl(self)
        self.profile = AsyncProfile(self)
        self.subject = AsyncSubject(self)
        self.trust_anchor = AsyncTrustAnchor(self)

    def operation_options(
        self, config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncRolesAnywhereClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self.config.get("operation_interceptors", [])
            ),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts",
                self.config.get("retry_max_attempts", DEFAULT_RETRY_MAX_ATTEMPTS),
            ),
            region=overrides.get("region", self.config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self.config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self.config.get("use_fips")),
            endpoint=overrides.get("endpoint", self.config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self.config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_rolesanywhere.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to the resource.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:ListTagsForResource</code>. </p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_notification_settings(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        notification_settings: "aws_sdk_rolesanywhere.types.notification_settings.NotificationSettings",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.put_notification_settings_response.PutNotificationSettingsResponse":
        """<p>Attaches a list of <i>notification settings</i> to a trust anchor.</p> <p>A notification setting includes information such as event name, threshold, status of the notification setting, and the channel to notify.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:PutNotificationSettings</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
            notification_settings: <p>A list of notification settings to be associated to the trust anchor.</p>

        Examples:
            PutNotificationSettings - Adds custom notification settings

            >>> await client.put_notification_settings(trust_anchor_id='c2505e61-2fc1-4a18-9fcf-94e18a22928b', notification_settings=[{'event': 'END_ENTITY_CERTIFICATE_EXPIRY', 'enabled': True, 'threshold': 10}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.put_notification_settings_request.PutNotificationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.put_notification_settings_response.PutNotificationSettingsResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.put_notification_settings

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.put_notification_settings.async_put_notification_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.put_notification_settings_request.PutNotificationSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["trust_anchor_id"] = trust_anchor_id
        input_["notification_settings"] = notification_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def reset_notification_settings(
        self,
        trust_anchor_id: "aws_sdk_rolesanywhere.types.uuid.Uuid",
        notification_setting_keys: "aws_sdk_rolesanywhere.types.notification_setting_keys.NotificationSettingKeys",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.reset_notification_settings_response.ResetNotificationSettingsResponse":
        """<p>Resets the <i>custom notification setting</i> to IAM Roles Anywhere default setting. </p> <p> <b>Required permissions: </b> <code>rolesanywhere:ResetNotificationSettings</code>. </p>

        Args:
            trust_anchor_id: <p>The unique identifier of the trust anchor.</p>
            notification_setting_keys: <p>A list of notification setting keys to reset. A notification setting key includes the event and the channel. </p>

        Examples:
            ResetNotificationSettings - Resets to IAM Roles Anywhere defined default notification settings

            >>> await client.reset_notification_settings(trust_anchor_id='c2505e61-2fc1-4a18-9fcf-94e18a22928b', notification_setting_keys=[{'event': 'END_ENTITY_CERTIFICATE_EXPIRY'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.reset_notification_settings_request.ResetNotificationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.reset_notification_settings_response.ResetNotificationSettingsResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.reset_notification_settings

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.reset_notification_settings.async_reset_notification_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.reset_notification_settings_request.ResetNotificationSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["trust_anchor_id"] = trust_anchor_id
        input_["notification_setting_keys"] = notification_setting_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_rolesanywhere.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_rolesanywhere.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.tag_resource_response.TagResourceResponse":
        """<p>Attaches tags to a resource.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:TagResource</code>. </p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The tags to attach to the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_rolesanywhere.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_rolesanywhere.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncRolesAnywhereClientConfig] = None,
    ) -> "aws_sdk_rolesanywhere.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the resource.</p> <p> <b>Required permissions: </b> <code>rolesanywhere:UntagResource</code>. </p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>A list of keys. Tag keys are the unique identifiers of tags. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_rolesanywhere.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_rolesanywhere.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_rolesanywhere._operations.roles_anywhere.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_rolesanywhere._operations.roles_anywhere.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_rolesanywhere.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
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
