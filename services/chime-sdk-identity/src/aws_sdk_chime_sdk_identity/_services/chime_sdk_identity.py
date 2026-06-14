"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ChimeIdentityService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_chime_sdk_identity._auth._signers
import aws_sdk_chime_sdk_identity._auth._sigv4
from aws_sdk_chime_sdk_identity._auth._identity import Credentials
from aws_sdk_chime_sdk_identity._auth._providers import (
    CredentialsProvider,
    StaticAwsCredentialsProvider,
)
from aws_sdk_chime_sdk_identity._auth._zapros_handler import AuthMiddleware
from aws_sdk_chime_sdk_identity._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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


class ChimeSDKIdentityClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: CredentialsProvider | None


DEFAULT_RETRY_MAX_ATTEMPTS = 3


def ensure_sync_iterator(it: Iterator[bytes] | bytes) -> Iterator[bytes]:
    if isinstance(it, bytes):
        yield it
    else:
        for chunk in it:
            yield chunk


class ChimeSDKIdentityClient:
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
        if credentials_provider is None and credentials is not None:
            credentials_provider = StaticAwsCredentialsProvider(credentials)
        self._config = ChimeSDKIdentityClientConfig(
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
        self, config_overrides: Optional[ChimeSDKIdentityClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ChimeSDKIdentityClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def create_app_instance(
        self,
        name: "aws_sdk_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName",
        client_request_token: "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.create_app_instance_request.CreateAppInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.create_app_instance_response.CreateAppInstanceResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance.create_app_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.create_app_instance_request.CreateAppInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["name"] = name
        if metadata is not None:
            input_["metadata"] = metadata
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_app_instance_admin(
        self,
        app_instance_admin_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.create_app_instance_admin_response.CreateAppInstanceAdminResponse":
        """<p>Promotes an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> to an <code>AppInstanceAdmin</code>. The promoted entity can perform the following actions. </p> <ul> <li> <p> <code>ChannelModerator</code> actions across all channels in the <code>AppInstance</code>.</p> </li> <li> <p> <code>DeleteChannelMessage</code> actions.</p> </li> </ul> <p>Only an <code>AppInstanceUser</code> and <code>AppInstanceBot</code> can be promoted to an <code>AppInstanceAdmin</code> role.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the administrator of the current <code>AppInstance</code>.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.create_app_instance_admin_request.CreateAppInstanceAdminRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.create_app_instance_admin_response.CreateAppInstanceAdminResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_admin

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_admin.create_app_instance_admin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.create_app_instance_admin_request.CreateAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_admin_arn"] = app_instance_admin_arn
        input_["app_instance_arn"] = app_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_app_instance_bot(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        client_request_token: "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        configuration: "aws_sdk_chime_sdk_identity.types.configuration.Configuration",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.create_app_instance_bot_request.CreateAppInstanceBotRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.create_app_instance_bot_response.CreateAppInstanceBotResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_bot

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_bot.create_app_instance_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.create_app_instance_bot_request.CreateAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
        if name is not None:
            input_["name"] = name
        if metadata is not None:
            input_["metadata"] = metadata
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_app_instance_user(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_user_id: "aws_sdk_chime_sdk_identity.types.user_id.UserId",
        name: "aws_sdk_chime_sdk_identity.types.user_name.UserName",
        client_request_token: "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.create_app_instance_user_request.CreateAppInstanceUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.create_app_instance_user_response.CreateAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_user

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.create_app_instance_user.create_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.create_app_instance_user_request.CreateAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
        input_["app_instance_user_id"] = app_instance_user_id
        input_["name"] = name
        if metadata is not None:
            input_["metadata"] = metadata
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if expiration_settings is not None:
            input_["expiration_settings"] = expiration_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_app_instance(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstance</code> and all associated data asynchronously.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.delete_app_instance_request.DeleteAppInstanceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance.delete_app_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.delete_app_instance_request.DeleteAppInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_app_instance_admin(
        self,
        app_instance_admin_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Demotes an <code>AppInstanceAdmin</code> to an <code>AppInstanceUser</code> or <code>AppInstanceBot</code>. This action does not delete the user.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the <code>AppInstance</code>'s administrator.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.delete_app_instance_admin_request.DeleteAppInstanceAdminRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_admin

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_admin.delete_app_instance_admin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.delete_app_instance_admin_request.DeleteAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_admin_arn"] = app_instance_admin_arn
        input_["app_instance_arn"] = app_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_app_instance_bot(
        self,
        app_instance_bot_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstanceBot</code>.</p>

        Args:
            app_instance_bot_arn: <p>The ARN of the <code>AppInstanceBot</code> being deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.delete_app_instance_bot_request.DeleteAppInstanceBotRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_bot

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_bot.delete_app_instance_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.delete_app_instance_bot_request.DeleteAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_bot_arn"] = app_instance_bot_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_app_instance_user(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deletes an <code>AppInstanceUser</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the user request being deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.delete_app_instance_user_request.DeleteAppInstanceUserRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_user

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.delete_app_instance_user.delete_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.delete_app_instance_user_request.DeleteAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def deregister_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_id: "aws_sdk_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Deregisters an <code>AppInstanceUserEndpoint</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            endpoint_id: <p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.deregister_app_instance_user_endpoint_request.DeregisterAppInstanceUserEndpointRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.deregister_app_instance_user_endpoint

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.deregister_app_instance_user_endpoint.deregister_app_instance_user_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.deregister_app_instance_user_endpoint_request.DeregisterAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn
        input_["endpoint_id"] = endpoint_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_app_instance(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_response.DescribeAppInstanceResponse":
        """<p>Returns the full details of an <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_request.DescribeAppInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_response.DescribeAppInstanceResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance.describe_app_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.describe_app_instance_request.DescribeAppInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_app_instance_admin(
        self,
        app_instance_admin_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_response.DescribeAppInstanceAdminResponse":
        """<p>Returns the full details of an <code>AppInstanceAdmin</code>.</p>

        Args:
            app_instance_admin_arn: <p>The ARN of the <code>AppInstanceAdmin</code>.</p>
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_request.DescribeAppInstanceAdminRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_response.DescribeAppInstanceAdminResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_admin

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_admin.describe_app_instance_admin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.describe_app_instance_admin_request.DescribeAppInstanceAdminRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_admin_arn"] = app_instance_admin_arn
        input_["app_instance_arn"] = app_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_app_instance_bot(
        self,
        app_instance_bot_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_response.DescribeAppInstanceBotResponse":
        """<p>The <code>AppInstanceBot's</code> information.</p>

        Args:
            app_instance_bot_arn: <p>The ARN of the <code>AppInstanceBot</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_request.DescribeAppInstanceBotRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_response.DescribeAppInstanceBotResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_bot

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_bot.describe_app_instance_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.describe_app_instance_bot_request.DescribeAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_bot_arn"] = app_instance_bot_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_app_instance_user(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_user_response.DescribeAppInstanceUserResponse":
        """<p>Returns the full details of an <code>AppInstanceUser</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_user_request.DescribeAppInstanceUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_user_response.DescribeAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user.describe_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.describe_app_instance_user_request.DescribeAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.string1600.String1600",
        endpoint_id: "aws_sdk_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_response.DescribeAppInstanceUserEndpointResponse":
        """<p>Returns the full details of an <code>AppInstanceUserEndpoint</code>.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            endpoint_id: <p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_request.DescribeAppInstanceUserEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_response.DescribeAppInstanceUserEndpointResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user_endpoint

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.describe_app_instance_user_endpoint.describe_app_instance_user_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.describe_app_instance_user_endpoint_request.DescribeAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn
        input_["endpoint_id"] = endpoint_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_app_instance_retention_settings(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_response.GetAppInstanceRetentionSettingsResponse":
        """<p>Gets the retention settings for an <code>AppInstance</code>.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_request.GetAppInstanceRetentionSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_response.GetAppInstanceRetentionSettingsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.get_app_instance_retention_settings

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.get_app_instance_retention_settings.get_app_instance_retention_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.get_app_instance_retention_settings_request.GetAppInstanceRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_app_instance_admins(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instance_admins_request.ListAppInstanceAdminsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instance_admins_response.ListAppInstanceAdminsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_admins

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_admins.list_app_instance_admins(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.list_app_instance_admins_request.ListAppInstanceAdminsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
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

    def list_app_instance_bots(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instance_bots_request.ListAppInstanceBotsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instance_bots_response.ListAppInstanceBotsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_bots

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_bots.list_app_instance_bots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.list_app_instance_bots_request.ListAppInstanceBotsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
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

    def list_app_instances(
        self,
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instances_request.ListAppInstancesRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instances_response.ListAppInstancesResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instances

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instances.list_app_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.list_app_instances_request.ListAppInstancesRequest = {}  # type: ignore[typeddict-item]
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

    def list_app_instance_user_endpoints(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_request.ListAppInstanceUserEndpointsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_response.ListAppInstanceUserEndpointsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_user_endpoints

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_user_endpoints.list_app_instance_user_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.list_app_instance_user_endpoints_request.ListAppInstanceUserEndpointsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn
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

    def list_app_instance_users(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.list_app_instance_users_request.ListAppInstanceUsersRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_app_instance_users_response.ListAppInstanceUsersResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_users

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_app_instance_users.list_app_instance_users(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.list_app_instance_users_request.ListAppInstanceUsersRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
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

    def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags applied to an Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_app_instance_retention_settings(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        app_instance_retention_settings: "aws_sdk_chime_sdk_identity.types.app_instance_retention_settings.AppInstanceRetentionSettings",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_response.PutAppInstanceRetentionSettingsResponse":
        """<p>Sets the amount of time in days that a given <code>AppInstance</code> retains data.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            app_instance_retention_settings: <p>The time in days to retain data. Data type: number.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_request.PutAppInstanceRetentionSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_response.PutAppInstanceRetentionSettingsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.put_app_instance_retention_settings

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.put_app_instance_retention_settings.put_app_instance_retention_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.put_app_instance_retention_settings_request.PutAppInstanceRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
        input_["app_instance_retention_settings"] = app_instance_retention_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_app_instance_user_expiration_settings(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
        expiration_settings: Optional[
            "aws_sdk_chime_sdk_identity.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_response.PutAppInstanceUserExpirationSettingsResponse":
        """<p>Sets the number of days before the <code>AppInstanceUser</code> is automatically deleted.</p> <note> <p>A background process deletes expired <code>AppInstanceUsers</code> within 6 hours of expiration. Actual deletion times may vary.</p> <p>Expired <code>AppInstanceUsers</code> that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.</p> </note>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            expiration_settings: <p>Settings that control the interval after which an <code>AppInstanceUser</code> is automatically deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_request.PutAppInstanceUserExpirationSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_response.PutAppInstanceUserExpirationSettingsResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.put_app_instance_user_expiration_settings

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.put_app_instance_user_expiration_settings.put_app_instance_user_expiration_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.put_app_instance_user_expiration_settings_request.PutAppInstanceUserExpirationSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn
        if expiration_settings is not None:
            input_["expiration_settings"] = expiration_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def register_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn",
        type: "aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_type.AppInstanceUserEndpointType",
        resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_attributes: "aws_sdk_chime_sdk_identity.types.endpoint_attributes.EndpointAttributes",
        client_request_token: "aws_sdk_chime_sdk_identity.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_request.RegisterAppInstanceUserEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_response.RegisterAppInstanceUserEndpointResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.register_app_instance_user_endpoint

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.register_app_instance_user_endpoint.register_app_instance_user_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.register_app_instance_user_endpoint_request.RegisterAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn
        if name is not None:
            input_["name"] = name
        input_["type"] = type
        input_["resource_arn"] = resource_arn
        input_["endpoint_attributes"] = endpoint_attributes
        input_["client_request_token"] = client_request_token
        if allow_messages is not None:
            input_["allow_messages"] = allow_messages

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        tags: "aws_sdk_chime_sdk_identity.types.tag_list.TagList",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Applies the specified tags to the specified Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tags: <p>The tag key-value pairs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.tag_resource

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def untag_resource(
        self,
        resource_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        tag_keys: "aws_sdk_chime_sdk_identity.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> None:
        """<p>Removes the specified tags from the specified Amazon Chime SDK identity resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tag_keys: <p>The tag keys.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.untag_resource

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_app_instance(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "aws_sdk_chime_sdk_identity.types.non_empty_resource_name.NonEmptyResourceName",
        metadata: "aws_sdk_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.update_app_instance_response.UpdateAppInstanceResponse":
        """<p>Updates <code>AppInstance</code> metadata.</p>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            name: <p>The name that you want to change.</p>
            metadata: <p>The metadata that you want to change.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.update_app_instance_request.UpdateAppInstanceRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.update_app_instance_response.UpdateAppInstanceResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance.update_app_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.update_app_instance_request.UpdateAppInstanceRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
        input_["name"] = name
        input_["metadata"] = metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_app_instance_bot(
        self,
        app_instance_bot_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "aws_sdk_chime_sdk_identity.types.resource_name.ResourceName",
        metadata: "aws_sdk_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.update_app_instance_bot_request.UpdateAppInstanceBotRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.update_app_instance_bot_response.UpdateAppInstanceBotResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_bot

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_bot.update_app_instance_bot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.update_app_instance_bot_request.UpdateAppInstanceBotRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_bot_arn"] = app_instance_bot_arn
        input_["name"] = name
        input_["metadata"] = metadata
        if configuration is not None:
            input_["configuration"] = configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_app_instance_user(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        name: "aws_sdk_chime_sdk_identity.types.user_name.UserName",
        metadata: "aws_sdk_chime_sdk_identity.types.metadata.Metadata",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_identity.types.update_app_instance_user_response.UpdateAppInstanceUserResponse":
        """<p>Updates the details of an <code>AppInstanceUser</code>. You can update names and metadata.</p>

        Args:
            app_instance_user_arn: <p>The ARN of the <code>AppInstanceUser</code>.</p>
            name: <p>The name of the <code>AppInstanceUser</code>.</p>
            metadata: <p>The metadata of the <code>AppInstanceUser</code>.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.update_app_instance_user_request.UpdateAppInstanceUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.update_app_instance_user_response.UpdateAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user.update_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.update_app_instance_user_request.UpdateAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn
        input_["name"] = name
        input_["metadata"] = metadata

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_app_instance_user_endpoint(
        self,
        app_instance_user_arn: "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn",
        endpoint_id: "aws_sdk_chime_sdk_identity.types.string64.String64",
        *,
        config_overrides: Optional[ChimeSDKIdentityClientConfig] = None,
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

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_request.UpdateAppInstanceUserEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_response.UpdateAppInstanceUserEndpointResponse"
        ]:
            import aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user_endpoint

            output, http_response = (
                aws_sdk_chime_sdk_identity._operations.chime_identity_service.update_app_instance_user_endpoint.update_app_instance_user_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_identity.types.update_app_instance_user_endpoint_request.UpdateAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_user_arn"] = app_instance_user_arn
        input_["endpoint_id"] = endpoint_id
        if name is not None:
            input_["name"] = name
        if allow_messages is not None:
            input_["allow_messages"] = allow_messages

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
