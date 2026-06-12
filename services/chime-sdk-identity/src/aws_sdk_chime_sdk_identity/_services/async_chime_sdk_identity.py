"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ChimeIdentityService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_chime_sdk_identity._auth._signers
import aws_sdk_chime_sdk_identity._auth._sigv4
from aws_sdk_chime_sdk_identity._auth._identity import Credentials
from aws_sdk_chime_sdk_identity._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_chime_sdk_identity._auth._zapros_handler import AuthMiddleware
from aws_sdk_chime_sdk_identity._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.allow_messages
    import aws_sdk_chime_sdk_identity.types.app_instance_retention_settings
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.client_request_token
    import aws_sdk_chime_sdk_identity.types.configuration
    import aws_sdk_chime_sdk_identity.types.create_app_instance_admin_request
    import aws_sdk_chime_sdk_identity.types.create_app_instance_admin_response
    import aws_sdk_chime_sdk_identity.types.create_app_instance_bot_request
    import aws_sdk_chime_sdk_identity.types.create_app_instance_bot_response
    import aws_sdk_chime_sdk_identity.types.create_app_instance_request
    import aws_sdk_chime_sdk_identity.types.create_app_instance_response
    import aws_sdk_chime_sdk_identity.types.create_app_instance_user_request
    import aws_sdk_chime_sdk_identity.types.create_app_instance_user_response
    import aws_sdk_chime_sdk_identity.types.delete_app_instance_admin_request
    import aws_sdk_chime_sdk_identity.types.delete_app_instance_bot_request
    import aws_sdk_chime_sdk_identity.types.delete_app_instance_request
    import aws_sdk_chime_sdk_identity.types.delete_app_instance_user_request
    import aws_sdk_chime_sdk_identity.types.deregister_app_instance_user_endpoint_request
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_request
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_response
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_request
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_response
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_request
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_response
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_request
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_response
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_user_request
    import aws_sdk_chime_sdk_identity.types.describe_app_instance_user_response
    import aws_sdk_chime_sdk_identity.types.endpoint_attributes
    import aws_sdk_chime_sdk_identity.types.expiration_settings
    import aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_request
    import aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_response
    import aws_sdk_chime_sdk_identity.types.list_app_instance_admins_request
    import aws_sdk_chime_sdk_identity.types.list_app_instance_admins_response
    import aws_sdk_chime_sdk_identity.types.list_app_instance_bots_request
    import aws_sdk_chime_sdk_identity.types.list_app_instance_bots_response
    import aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_request
    import aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_response
    import aws_sdk_chime_sdk_identity.types.list_app_instance_users_request
    import aws_sdk_chime_sdk_identity.types.list_app_instance_users_response
    import aws_sdk_chime_sdk_identity.types.list_app_instances_request
    import aws_sdk_chime_sdk_identity.types.list_app_instances_response
    import aws_sdk_chime_sdk_identity.types.list_tags_for_resource_request
    import aws_sdk_chime_sdk_identity.types.list_tags_for_resource_response
    import aws_sdk_chime_sdk_identity.types.max_results
    import aws_sdk_chime_sdk_identity.types.metadata
    import aws_sdk_chime_sdk_identity.types.next_token
    import aws_sdk_chime_sdk_identity.types.non_empty_resource_name
    import aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_request
    import aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_response
    import aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_request
    import aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_response
    import aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_request
    import aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_response
    import aws_sdk_chime_sdk_identity.types.resource_name
    import aws_sdk_chime_sdk_identity.types.sensitive_chime_arn
    import aws_sdk_chime_sdk_identity.types.sensitive_string1600
    import aws_sdk_chime_sdk_identity.types.string64
    import aws_sdk_chime_sdk_identity.types.string1600
    import aws_sdk_chime_sdk_identity.types.tag_key_list
    import aws_sdk_chime_sdk_identity.types.tag_list
    import aws_sdk_chime_sdk_identity.types.tag_resource_request
    import aws_sdk_chime_sdk_identity.types.untag_resource_request
    import aws_sdk_chime_sdk_identity.types.update_app_instance_bot_request
    import aws_sdk_chime_sdk_identity.types.update_app_instance_bot_response
    import aws_sdk_chime_sdk_identity.types.update_app_instance_request
    import aws_sdk_chime_sdk_identity.types.update_app_instance_response
    import aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_request
    import aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_response
    import aws_sdk_chime_sdk_identity.types.update_app_instance_user_request
    import aws_sdk_chime_sdk_identity.types.update_app_instance_user_response
    import aws_sdk_chime_sdk_identity.types.user_id
    import aws_sdk_chime_sdk_identity.types.user_name


class AsyncChimeSDKIdentityClientConfig(TypedDict, total=False):
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


class AsyncChimeSDKIdentityClient:
    """A client for the ``ChimeSDKIdentity`` service.

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
        self.config = AsyncChimeSDKIdentityClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncChimeSDKIdentityClientConfig = config_overrides or {}
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

    async def create_app_instance(
        self,
        name: "aws_sdk_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName",
        client_request_token: "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        metadata: Optional["aws_sdk_chime_sdk_identity.types.metadata.Metadata"] = None,
        tags: Optional["aws_sdk_chime_sdk_identity.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.create_app_instance_response.CreateAppInstanceResponse":
        """<p>Creates an Amazon Chime SDK messaging <code>AppInstance</code> under an AWS account. Only SDK messaging customers use this API. <code>CreateAppInstance</code> supports idempotency behavior as described in the AWS API Standard.</p> <p>identity</p>

        Args:
            name: <p>The name of the <code>AppInstance</code>.</p>
            metadata: <p>The metadata of the <code>AppInstance</code>. Limited to a 1KB string in UTF-8.</p>
            client_request_token: <p>The unique ID of the request. Use different tokens to create different <code>AppInstances</code>.</p>
            tags: <p>Tags assigned to the <code>AppInstance</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.create_app_instance_request.CreateAppInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.create_app_instance_response.CreateAppInstanceResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance.async_create_app_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.create_app_instance_request.CreateAppInstanceRequest = {}  # type: ignore[typeddict-item]
        input["name"] = name
        if metadata is not None:
            input["metadata"] = metadata
        input["client_request_token"] = client_request_token
        if tags is not None:
            input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_app_instance_admin(
        self,
        app_instance_admin_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.create_app_instance_admin_response.CreateAppInstanceAdminResponse":
        """<p>Promotes an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> to an <code>AppInstanceAdmin</code>. The promoted entity can perform the following actions. </p> <ul> <li> <p> <code>ChannelModerator</code> actions across all channels in the <code>AppInstance</code>.</p> </li> <li> <p> <code>DeleteChannelMessage</code> actions.</p> </li> </ul> <p>Only an <code>AppInstanceUser</code> and <code>AppInstanceBot</code> can be promoted to an <code>AppInstanceAdmin</code> role.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the administrator of the current <code>AppInstance</code>.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.create_app_instance_admin_request.CreateAppInstanceAdminRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.create_app_instance_admin_response.CreateAppInstanceAdminResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_admin

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_admin.async_create_app_instance_admin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.create_app_instance_admin_request.CreateAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_admin_arn"] = app_instance_admin_arn
        input["app_instance_arn"] = app_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_app_instance_bot(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        client_request_token: "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        configuration: "aws_sdk_chime_sdk_identity.types.configuration.Configuration",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        name: Optional[
            "aws_sdk_chime_sdk_identity.types.resource_name.ResourceName"
        ] = None,
        metadata: Optional["aws_sdk_chime_sdk_identity.types.metadata.Metadata"] = None,
        tags: Optional["aws_sdk_chime_sdk_identity.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.create_app_instance_bot_response.CreateAppInstanceBotResponse":
        """<p>Creates a bot under an Amazon Chime <code>AppInstance</code>. The request consists of a unique <code>Configuration</code> and <code>Name</code> for that bot.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code> request.</p>
            name: <p>The user's name.</p>
            metadata: <p>The request metadata. Limited to a 1KB string in UTF-8.</p>
            client_request_token: <p>The unique ID for the client making the request. Use different tokens for different <code>AppInstanceBots</code>.</p>
            tags: <p>The tags assigned to the <code>AppInstanceBot</code>.</p>
            configuration: <p>Configuration information about the Amazon Lex V2 V2 bot.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.create_app_instance_bot_request.CreateAppInstanceBotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.create_app_instance_bot_response.CreateAppInstanceBotResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_bot

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_bot.async_create_app_instance_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.create_app_instance_bot_request.CreateAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn
        if name is not None:
            input["name"] = name
        if metadata is not None:
            input["metadata"] = metadata
        input["client_request_token"] = client_request_token
        if tags is not None:
            input["tags"] = tags
        input["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_app_instance_user(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_user_id: "aws_sdk_chime_sdk_identity.types.user_id.UserId",
        name: "aws_sdk_chime_sdk_identity.types.user_name.UserName",
        client_request_token: "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        metadata: Optional["aws_sdk_chime_sdk_identity.types.metadata.Metadata"] = None,
        tags: Optional["aws_sdk_chime_sdk_identity.types.tag_list.TagList"] = None,
        expiration_settings: Optional[
            "aws_sdk_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.create_app_instance_user_response.CreateAppInstanceUserResponse":
        """<p>Creates a user under an Amazon Chime <code>AppInstance</code>. The request consists of a unique <code>appInstanceUserId</code> and <code>Name</code> for that user.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code> request.</p>
            app_instance_user_id: <p>The user ID of the <code>AppInstance</code>.</p>
            name: <p>The user's name.</p>
            metadata: <p>The request's metadata. Limited to a 1KB string in UTF-8.</p>
            client_request_token: <p>The unique ID of the request. Use different tokens to request additional <code>AppInstances</code>.</p>
            tags: <p>Tags assigned to the <code>AppInstanceUser</code>.</p>
            expiration_settings: <p>Settings that control the interval after which the <code>AppInstanceUser</code> is automatically deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.create_app_instance_user_request.CreateAppInstanceUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.create_app_instance_user_response.CreateAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_user

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_user.async_create_app_instance_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.create_app_instance_user_request.CreateAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn
        input["app_instance_user_id"] = app_instance_user_id
        input["name"] = name
        if metadata is not None:
            input["metadata"] = metadata
        input["client_request_token"] = client_request_token
        if tags is not None:
            input["tags"] = tags
        if expiration_settings is not None:
            input["expiration_settings"] = expiration_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_app_instance(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstance</code> and all associated data asynchronously.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.delete_app_instance_request.DeleteAppInstanceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance.async_delete_app_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.delete_app_instance_request.DeleteAppInstanceRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_app_instance_admin(
        self,
        app_instance_admin_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Demotes an <code>AppInstanceAdmin</code> to an <code>AppInstanceUser</code> or <code>AppInstanceBot</code>. This action does not delete the user.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the <code>AppInstance</code>'s administrator.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.delete_app_instance_admin_request.DeleteAppInstanceAdminRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_admin

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_admin.async_delete_app_instance_admin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.delete_app_instance_admin_request.DeleteAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_admin_arn"] = app_instance_admin_arn
        input["app_instance_arn"] = app_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_app_instance_bot(
        self,
        app_instance_bot_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstanceBot</code>.</p>

        Args:
            app_instance_bot_arn: <p>The ARN of the <code>AppInstanceBot</code> being deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.delete_app_instance_bot_request.DeleteAppInstanceBotRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_bot

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_bot.async_delete_app_instance_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.delete_app_instance_bot_request.DeleteAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_bot_arn"] = app_instance_bot_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_app_instance_user(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstanceUser</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the user request being deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.delete_app_instance_user_request.DeleteAppInstanceUserRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_user

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_user.async_delete_app_instance_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.delete_app_instance_user_request.DeleteAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def deregister_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_id: "aws_sdk_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deregisters an <code>AppInstanceUserEndpoint</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            endpoint_id: <p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.deregister_app_instance_user_endpoint_request.DeregisterAppInstanceUserEndpointRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.deregister_app_instance_user_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.deregister_app_instance_user_endpoint.async_deregister_app_instance_user_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.deregister_app_instance_user_endpoint_request.DeregisterAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn
        input["endpoint_id"] = endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_app_instance(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_response.DescribeAppInstanceResponse":
        """<p>Returns the full details of an <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_request.DescribeAppInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_response.DescribeAppInstanceResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance.async_describe_app_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.describe_app_instance_request.DescribeAppInstanceRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_app_instance_admin(
        self,
        app_instance_admin_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_response.DescribeAppInstanceAdminResponse":
        """<p>Returns the full details of an <code>AppInstanceAdmin</code>.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the <code>AppInstanceAdmin</code>.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_request.DescribeAppInstanceAdminRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_response.DescribeAppInstanceAdminResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_admin

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_admin.async_describe_app_instance_admin(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_request.DescribeAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_admin_arn"] = app_instance_admin_arn
        input["app_instance_arn"] = app_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_app_instance_bot(
        self,
        app_instance_bot_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_response.DescribeAppInstanceBotResponse":
        """<p>The <code>AppInstanceBot's</code> information.</p>

        Args:
            app_instance_bot_arn: <p>The ARN of the <code>AppInstanceBot</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_request.DescribeAppInstanceBotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_response.DescribeAppInstanceBotResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_bot

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_bot.async_describe_app_instance_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_request.DescribeAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_bot_arn"] = app_instance_bot_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_app_instance_user(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_user_response.DescribeAppInstanceUserResponse":
        """<p>Returns the full details of an <code>AppInstanceUser</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_user_request.DescribeAppInstanceUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_user_response.DescribeAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user.async_describe_app_instance_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.describe_app_instance_user_request.DescribeAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.string1600.String1600",
        endpoint_id: "aws_sdk_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_response.DescribeAppInstanceUserEndpointResponse":
        """<p>Returns the full details of an <code>AppInstanceUserEndpoint</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            endpoint_id: <p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_request.DescribeAppInstanceUserEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_response.DescribeAppInstanceUserEndpointResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user_endpoint.async_describe_app_instance_user_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_request.DescribeAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn
        input["endpoint_id"] = endpoint_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_app_instance_retention_settings(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_response.GetAppInstanceRetentionSettingsResponse":
        """<p>Gets the retention settings for an <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_request.GetAppInstanceRetentionSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_response.GetAppInstanceRetentionSettingsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.get_app_instance_retention_settings

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.get_app_instance_retention_settings.async_get_app_instance_retention_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_request.GetAppInstanceRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_app_instance_admins(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.list_app_instance_admins_response.ListAppInstanceAdminsResponse":
        """<p>Returns a list of the administrators in the <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            max_results: <p>The maximum number of administrators that you want to return.</p>
            next_token: <p>The token returned from previous API requests until the number of administrators is reached.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instance_admins_request.ListAppInstanceAdminsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instance_admins_response.ListAppInstanceAdminsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_admins

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_admins.async_list_app_instance_admins(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.list_app_instance_admins_request.ListAppInstanceAdminsRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_app_instance_bots(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.list_app_instance_bots_response.ListAppInstanceBotsResponse":
        """<p>Lists all <code>AppInstanceBots</code> created under a single <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            max_results: <p>The maximum number of requests to return.</p>
            next_token: <p>The token passed by previous API calls until all requested bots are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instance_bots_request.ListAppInstanceBotsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instance_bots_response.ListAppInstanceBotsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_bots

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_bots.async_list_app_instance_bots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.list_app_instance_bots_request.ListAppInstanceBotsRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_app_instances(
        self,
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.list_app_instances_response.ListAppInstancesResponse":
        """<p>Lists all Amazon Chime <code>AppInstance</code>s created under a single AWS account.</p>

        Args:
            max_results: <p>The maximum number of <code>AppInstance</code>s that you want to return.</p>
            next_token: <p>The token passed by previous API requests until you reach the maximum number of <code>AppInstances</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instances_request.ListAppInstancesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instances_response.ListAppInstancesResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instances

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instances.async_list_app_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.list_app_instances_request.ListAppInstancesRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_app_instance_user_endpoints(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_response.ListAppInstanceUserEndpointsResponse":
        """<p>Lists all the <code>AppInstanceUserEndpoints</code> created under a single <code>AppInstanceUser</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            max_results: <p>The maximum number of endpoints that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested endpoints are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_request.ListAppInstanceUserEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_response.ListAppInstanceUserEndpointsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_user_endpoints

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_user_endpoints.async_list_app_instance_user_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_request.ListAppInstanceUserEndpointsRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_app_instance_users(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_identity.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_identity.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.list_app_instance_users_response.ListAppInstanceUsersResponse":
        """<p>List all <code>AppInstanceUsers</code> created under a single <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            max_results: <p>The maximum number of requests that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested users are returned.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instance_users_request.ListAppInstanceUsersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instance_users_response.ListAppInstanceUsersResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_users

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_users.async_list_app_instance_users(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.list_app_instance_users_request.ListAppInstanceUsersRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn
        if max_results is not None:
            input["max_results"] = max_results
        if next_token is not None:
            input["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags applied to an Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_app_instance_retention_settings(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_retention_settings: "aws_sdk_chime_sdk_identity.types.app_instance_retention_settings.AppInstanceRetentionSettings",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_response.PutAppInstanceRetentionSettingsResponse":
        """<p>Sets the amount of time in days that a given <code>AppInstance</code> retains data.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            app_instance_retention_settings: <p>The time in days to retain data. Data type: number.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_request.PutAppInstanceRetentionSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_response.PutAppInstanceRetentionSettingsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.put_app_instance_retention_settings

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.put_app_instance_retention_settings.async_put_app_instance_retention_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_request.PutAppInstanceRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn
        input["app_instance_retention_settings"] = app_instance_retention_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def put_app_instance_user_expiration_settings(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        expiration_settings: Optional[
            "aws_sdk_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_response.PutAppInstanceUserExpirationSettingsResponse":
        """<p>Sets the number of days before the <code>AppInstanceUser</code> is automatically deleted.</p> <note> <p>A background process deletes expired <code>AppInstanceUsers</code> within 6 hours of expiration. Actual deletion times may vary.</p> <p>Expired <code>AppInstanceUsers</code> that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.</p> </note>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            expiration_settings: <p>Settings that control the interval after which an <code>AppInstanceUser</code> is automatically deleted.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_request.PutAppInstanceUserExpirationSettingsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_response.PutAppInstanceUserExpirationSettingsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.put_app_instance_user_expiration_settings

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.put_app_instance_user_expiration_settings.async_put_app_instance_user_expiration_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_request.PutAppInstanceUserExpirationSettingsRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn
        if expiration_settings is not None:
            input["expiration_settings"] = expiration_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def register_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn",
        type: "aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type.AppInstanceUserEndpointType",
        resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_attributes: "aws_sdk_chime_sdk_identity.types.endpoint_attributes.EndpointAttributes",
        client_request_token: "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        name: Optional[
            "aws_sdk_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
        ] = None,
        allow_messages: Optional[
            "aws_sdk_chime_sdk_identity.types.allow_messages.AllowMessages"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_response.RegisterAppInstanceUserEndpointResponse":
        """<p>Registers an endpoint under an Amazon Chime <code>AppInstanceUser</code>. The endpoint receives messages for a user. For push notifications, the endpoint is a mobile device used to receive mobile push notifications for a user.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            name: <p>The name of the <code>AppInstanceUserEndpoint</code>.</p>
            type: <p>The type of the <code>AppInstanceUserEndpoint</code>. Supported types:</p> <ul> <li> <p> <code>APNS</code>: The mobile notification service for an Apple device.</p> </li> <li> <p> <code>APNS_SANDBOX</code>: The sandbox environment of the mobile notification service for an Apple device.</p> </li> <li> <p> <code>GCM</code>: The mobile notification service for an Android device.</p> </li> </ul> <p>Populate the <code>ResourceArn</code> value of each type as <code>PinpointAppArn</code>.</p>
            resource_arn: <p>The ARN of the resource to which the endpoint belongs.</p>
            endpoint_attributes: <p>The attributes of an <code>Endpoint</code>.</p>
            client_request_token: <p>The unique ID assigned to the request. Use different tokens to register other endpoints.</p>
            allow_messages: <p>Boolean that controls whether the AppInstanceUserEndpoint is opted in to receive messages. <code>ALL</code> indicates the endpoint receives all messages. <code>NONE</code> indicates the endpoint receives no messages.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_request.RegisterAppInstanceUserEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_response.RegisterAppInstanceUserEndpointResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.register_app_instance_user_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.register_app_instance_user_endpoint.async_register_app_instance_user_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_request.RegisterAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn
        if name is not None:
            input["name"] = name
        input["type"] = type
        input["resource_arn"] = resource_arn
        input["endpoint_attributes"] = endpoint_attributes
        input["client_request_token"] = client_request_token
        if allow_messages is not None:
            input["allow_messages"] = allow_messages

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        tags: "aws_sdk_chime_sdk_identity.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Applies the specified tags to the specified Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tags: <p>The tag key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def untag_resource(
        self,
        resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        tag_keys: "aws_sdk_chime_sdk_identity.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Removes the specified tags from the specified Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tag_keys: <p>The tag keys.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input["resource_arn"] = resource_arn
        input["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_app_instance(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "aws_sdk_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName",
        metadata: "aws_sdk_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.update_app_instance_response.UpdateAppInstanceResponse":
        """<p>Updates <code>AppInstance</code> metadata.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            name: <p>The name that you want to change.</p>
            metadata: <p>The metadata that you want to change.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.update_app_instance_request.UpdateAppInstanceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.update_app_instance_response.UpdateAppInstanceResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance.async_update_app_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.update_app_instance_request.UpdateAppInstanceRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_arn"] = app_instance_arn
        input["name"] = name
        input["metadata"] = metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_app_instance_bot(
        self,
        app_instance_bot_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "aws_sdk_chime_sdk_identity.types.resource_name.ResourceName",
        metadata: "aws_sdk_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        configuration: Optional[
            "aws_sdk_chime_sdk_identity.types.configuration.Configuration"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.update_app_instance_bot_response.UpdateAppInstanceBotResponse":
        """<p>Updates the name and metadata of an <code>AppInstanceBot</code>.</p>

        Args:
            app_instance_bot_arn: <p>The ARN of the <code>AppInstanceBot</code>.</p>
            name: <p>The name of the <code>AppInstanceBot</code>.</p>
            metadata: <p>The metadata of the <code>AppInstanceBot</code>.</p>
            configuration: <p>The configuration for the bot update.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.update_app_instance_bot_request.UpdateAppInstanceBotRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.update_app_instance_bot_response.UpdateAppInstanceBotResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_bot

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_bot.async_update_app_instance_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.update_app_instance_bot_request.UpdateAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_bot_arn"] = app_instance_bot_arn
        input["name"] = name
        input["metadata"] = metadata
        if configuration is not None:
            input["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_app_instance_user(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "aws_sdk_chime_sdk_identity.types.user_name.UserName",
        metadata: "aws_sdk_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.update_app_instance_user_response.UpdateAppInstanceUserResponse":
        """<p>Updates the details of an <code>AppInstanceUser</code>. You can update names and metadata.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            name: <p>The name of the <code>AppInstanceUser</code>.</p>
            metadata: <p>The metadata of the <code>AppInstanceUser</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.update_app_instance_user_request.UpdateAppInstanceUserRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.update_app_instance_user_response.UpdateAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user.async_update_app_instance_user(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.update_app_instance_user_request.UpdateAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn
        input["name"] = name
        input["metadata"] = metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_id: "aws_sdk_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[AsyncChimeSDKIdentityClientConfig] = None,
        name: Optional[
            "aws_sdk_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
        ] = None,
        allow_messages: Optional[
            "aws_sdk_chime_sdk_identity.types.allow_messages.AllowMessages"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_response.UpdateAppInstanceUserEndpointResponse":
        """<p>Updates the details of an <code>AppInstanceUserEndpoint</code>. You can update the name and <code>AllowMessage</code> values.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            endpoint_id: <p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>
            name: <p>The name of the <code>AppInstanceUserEndpoint</code>.</p>
            allow_messages: <p>Boolean that controls whether the <code>AppInstanceUserEndpoint</code> is opted in to receive messages. <code>ALL</code> indicates the endpoint will receive all messages. <code>NONE</code> indicates the endpoint will receive no messages.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_request.UpdateAppInstanceUserEndpointRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_response.UpdateAppInstanceUserEndpointResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user_endpoint

            (
                output,
                http_response,
            ) = await aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user_endpoint.async_update_app_instance_user_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input: aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_request.UpdateAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
        input["app_instance_user_arn"] = app_instance_user_arn
        input["endpoint_id"] = endpoint_id
        if name is not None:
            input["name"] = name
        if allow_messages is not None:
            input["allow_messages"] = allow_messages

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
