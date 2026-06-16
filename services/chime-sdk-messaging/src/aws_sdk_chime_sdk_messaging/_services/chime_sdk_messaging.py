"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChimeMessagingService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import BaseHandler, Client

import aws_sdk_chime_sdk_messaging._auth._signers
import aws_sdk_chime_sdk_messaging._auth._sigv4
from aws_sdk_chime_sdk_messaging._auth._identity import Credentials
from aws_sdk_chime_sdk_messaging._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_chime_sdk_messaging._auth._zapros_handler import AuthMiddleware
from aws_sdk_chime_sdk_messaging._services._aws_config import aws_config
from aws_sdk_chime_sdk_messaging._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.associate_channel_flow_request
    import aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_request
    import aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_response
    import aws_sdk_chime_sdk_messaging.types.callback_id_type
    import aws_sdk_chime_sdk_messaging.types.channel_flow_callback_request
    import aws_sdk_chime_sdk_messaging.types.channel_flow_callback_response
    import aws_sdk_chime_sdk_messaging.types.channel_id
    import aws_sdk_chime_sdk_messaging.types.channel_member_arns
    import aws_sdk_chime_sdk_messaging.types.channel_membership_preferences
    import aws_sdk_chime_sdk_messaging.types.channel_membership_type
    import aws_sdk_chime_sdk_messaging.types.channel_message_callback
    import aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type
    import aws_sdk_chime_sdk_messaging.types.channel_message_type
    import aws_sdk_chime_sdk_messaging.types.channel_mode
    import aws_sdk_chime_sdk_messaging.types.channel_moderator_arns
    import aws_sdk_chime_sdk_messaging.types.channel_privacy
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.client_request_token
    import aws_sdk_chime_sdk_messaging.types.content_type
    import aws_sdk_chime_sdk_messaging.types.create_channel_ban_request
    import aws_sdk_chime_sdk_messaging.types.create_channel_ban_response
    import aws_sdk_chime_sdk_messaging.types.create_channel_flow_request
    import aws_sdk_chime_sdk_messaging.types.create_channel_flow_response
    import aws_sdk_chime_sdk_messaging.types.create_channel_membership_request
    import aws_sdk_chime_sdk_messaging.types.create_channel_membership_response
    import aws_sdk_chime_sdk_messaging.types.create_channel_moderator_request
    import aws_sdk_chime_sdk_messaging.types.create_channel_moderator_response
    import aws_sdk_chime_sdk_messaging.types.create_channel_request
    import aws_sdk_chime_sdk_messaging.types.create_channel_response
    import aws_sdk_chime_sdk_messaging.types.delete_channel_ban_request
    import aws_sdk_chime_sdk_messaging.types.delete_channel_flow_request
    import aws_sdk_chime_sdk_messaging.types.delete_channel_membership_request
    import aws_sdk_chime_sdk_messaging.types.delete_channel_message_request
    import aws_sdk_chime_sdk_messaging.types.delete_channel_moderator_request
    import aws_sdk_chime_sdk_messaging.types.delete_channel_request
    import aws_sdk_chime_sdk_messaging.types.delete_messaging_streaming_configurations_request
    import aws_sdk_chime_sdk_messaging.types.describe_channel_ban_request
    import aws_sdk_chime_sdk_messaging.types.describe_channel_ban_response
    import aws_sdk_chime_sdk_messaging.types.describe_channel_flow_request
    import aws_sdk_chime_sdk_messaging.types.describe_channel_flow_response
    import aws_sdk_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_request
    import aws_sdk_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_response
    import aws_sdk_chime_sdk_messaging.types.describe_channel_membership_request
    import aws_sdk_chime_sdk_messaging.types.describe_channel_membership_response
    import aws_sdk_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request
    import aws_sdk_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response
    import aws_sdk_chime_sdk_messaging.types.describe_channel_moderator_request
    import aws_sdk_chime_sdk_messaging.types.describe_channel_moderator_response
    import aws_sdk_chime_sdk_messaging.types.describe_channel_request
    import aws_sdk_chime_sdk_messaging.types.describe_channel_response
    import aws_sdk_chime_sdk_messaging.types.disassociate_channel_flow_request
    import aws_sdk_chime_sdk_messaging.types.elastic_channel_configuration
    import aws_sdk_chime_sdk_messaging.types.expiration_settings
    import aws_sdk_chime_sdk_messaging.types.get_channel_membership_preferences_request
    import aws_sdk_chime_sdk_messaging.types.get_channel_membership_preferences_response
    import aws_sdk_chime_sdk_messaging.types.get_channel_message_request
    import aws_sdk_chime_sdk_messaging.types.get_channel_message_response
    import aws_sdk_chime_sdk_messaging.types.get_channel_message_status_request
    import aws_sdk_chime_sdk_messaging.types.get_channel_message_status_response
    import aws_sdk_chime_sdk_messaging.types.get_messaging_session_endpoint_request
    import aws_sdk_chime_sdk_messaging.types.get_messaging_session_endpoint_response
    import aws_sdk_chime_sdk_messaging.types.get_messaging_streaming_configurations_request
    import aws_sdk_chime_sdk_messaging.types.get_messaging_streaming_configurations_response
    import aws_sdk_chime_sdk_messaging.types.list_channel_bans_request
    import aws_sdk_chime_sdk_messaging.types.list_channel_bans_response
    import aws_sdk_chime_sdk_messaging.types.list_channel_flows_request
    import aws_sdk_chime_sdk_messaging.types.list_channel_flows_response
    import aws_sdk_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_request
    import aws_sdk_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_response
    import aws_sdk_chime_sdk_messaging.types.list_channel_memberships_request
    import aws_sdk_chime_sdk_messaging.types.list_channel_memberships_response
    import aws_sdk_chime_sdk_messaging.types.list_channel_messages_request
    import aws_sdk_chime_sdk_messaging.types.list_channel_messages_response
    import aws_sdk_chime_sdk_messaging.types.list_channel_moderators_request
    import aws_sdk_chime_sdk_messaging.types.list_channel_moderators_response
    import aws_sdk_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_request
    import aws_sdk_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_response
    import aws_sdk_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_request
    import aws_sdk_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_response
    import aws_sdk_chime_sdk_messaging.types.list_channels_request
    import aws_sdk_chime_sdk_messaging.types.list_channels_response
    import aws_sdk_chime_sdk_messaging.types.list_sub_channels_request
    import aws_sdk_chime_sdk_messaging.types.list_sub_channels_response
    import aws_sdk_chime_sdk_messaging.types.list_tags_for_resource_request
    import aws_sdk_chime_sdk_messaging.types.list_tags_for_resource_response
    import aws_sdk_chime_sdk_messaging.types.max_results
    import aws_sdk_chime_sdk_messaging.types.member_arns
    import aws_sdk_chime_sdk_messaging.types.message_attribute_map
    import aws_sdk_chime_sdk_messaging.types.message_id
    import aws_sdk_chime_sdk_messaging.types.metadata
    import aws_sdk_chime_sdk_messaging.types.network_type
    import aws_sdk_chime_sdk_messaging.types.next_token
    import aws_sdk_chime_sdk_messaging.types.non_empty_content
    import aws_sdk_chime_sdk_messaging.types.non_empty_resource_name
    import aws_sdk_chime_sdk_messaging.types.non_nullable_boolean
    import aws_sdk_chime_sdk_messaging.types.processor_list
    import aws_sdk_chime_sdk_messaging.types.push_notification_configuration
    import aws_sdk_chime_sdk_messaging.types.put_channel_expiration_settings_request
    import aws_sdk_chime_sdk_messaging.types.put_channel_expiration_settings_response
    import aws_sdk_chime_sdk_messaging.types.put_channel_membership_preferences_request
    import aws_sdk_chime_sdk_messaging.types.put_channel_membership_preferences_response
    import aws_sdk_chime_sdk_messaging.types.put_messaging_streaming_configurations_request
    import aws_sdk_chime_sdk_messaging.types.put_messaging_streaming_configurations_response
    import aws_sdk_chime_sdk_messaging.types.redact_channel_message_request
    import aws_sdk_chime_sdk_messaging.types.redact_channel_message_response
    import aws_sdk_chime_sdk_messaging.types.search_channels_request
    import aws_sdk_chime_sdk_messaging.types.search_channels_response
    import aws_sdk_chime_sdk_messaging.types.search_fields
    import aws_sdk_chime_sdk_messaging.types.send_channel_message_request
    import aws_sdk_chime_sdk_messaging.types.send_channel_message_response
    import aws_sdk_chime_sdk_messaging.types.sort_order
    import aws_sdk_chime_sdk_messaging.types.streaming_configuration_list
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id
    import aws_sdk_chime_sdk_messaging.types.tag_key_list
    import aws_sdk_chime_sdk_messaging.types.tag_list
    import aws_sdk_chime_sdk_messaging.types.tag_resource_request
    import aws_sdk_chime_sdk_messaging.types.target_list
    import aws_sdk_chime_sdk_messaging.types.timestamp
    import aws_sdk_chime_sdk_messaging.types.untag_resource_request
    import aws_sdk_chime_sdk_messaging.types.update_channel_flow_request
    import aws_sdk_chime_sdk_messaging.types.update_channel_flow_response
    import aws_sdk_chime_sdk_messaging.types.update_channel_message_request
    import aws_sdk_chime_sdk_messaging.types.update_channel_message_response
    import aws_sdk_chime_sdk_messaging.types.update_channel_read_marker_request
    import aws_sdk_chime_sdk_messaging.types.update_channel_read_marker_response
    import aws_sdk_chime_sdk_messaging.types.update_channel_request
    import aws_sdk_chime_sdk_messaging.types.update_channel_response


class ChimeSDKMessagingClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ChimeSDKMessagingClient:
    """A client for the ``ChimeSDKMessaging`` service.

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
        self._config = ChimeSDKMessagingClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[ChimeSDKMessagingClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ChimeSDKMessagingClientConfig = config_overrides or {}
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

    def associate_channel_flow(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Associates a channel flow with a channel. Once associated, all messages to that channel go through channel flow processors. To stop processing, use the <code>DisassociateChannelFlow</code> API.</p> <note> <p>Only administrators or channel moderators can associate a channel flow. The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_flow_arn: <p>The ARN of the channel flow.</p>
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.associate_channel_flow_request.AssociateChannelFlowRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.associate_channel_flow

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.associate_channel_flow.associate_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.associate_channel_flow_request.AssociateChannelFlowRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["channel_flow_arn"] = channel_flow_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def batch_create_channel_membership(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arns: "aws_sdk_chime_sdk_messaging.types.member_arns.MemberArns",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        type: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
        ] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_response.BatchCreateChannelMembershipResponse":
        """<p>Adds a specified number of users and bots to a channel. </p>

        Args:
            channel_arn: <p>The ARN of the channel to which you're adding users or bots.</p>
            type: <p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned. This is only supported by moderators.</p>
            member_arns: <p>The ARNs of the members you want to add to the channel. Only <code>AppInstanceUsers</code> and <code>AppInstanceBots</code> can be added as a channel member.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request. </p> <note> <p>Only required when creating membership in a SubChannel for a moderator in an elastic channel.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_request.BatchCreateChannelMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_response.BatchCreateChannelMembershipResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.batch_create_channel_membership

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.batch_create_channel_membership.batch_create_channel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.batch_create_channel_membership_request.BatchCreateChannelMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if type is not None:
            input_["type"] = type
        input_["member_arns"] = member_arns
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def channel_flow_callback(
        self,
        callback_id: "aws_sdk_chime_sdk_messaging.types.callback_id_type.CallbackIdType",
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_message: "aws_sdk_chime_sdk_messaging.types.channel_message_callback.ChannelMessageCallback",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        delete_resource: Optional[
            "aws_sdk_chime_sdk_messaging.types.non_nullable_boolean.NonNullableBoolean"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.channel_flow_callback_response.ChannelFlowCallbackResponse":
        """<p>Calls back Amazon Chime SDK messaging with a processing response message. This should be invoked from the processor Lambda. This is a developer API.</p> <p>You can return one of the following processing responses:</p> <ul> <li> <p>Update message content or metadata</p> </li> <li> <p>Deny a message</p> </li> <li> <p>Make no changes to the message</p> </li> </ul>

        Args:
            callback_id: <p>The identifier passed to the processor by the service when invoked. Use the identifier to call back the service.</p>
            channel_arn: <p>The ARN of the channel.</p>
            delete_resource: <p>When a processor determines that a message needs to be <code>DENIED</code>, pass this parameter with a value of true.</p>
            channel_message: <p>Stores information about the processed message.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.channel_flow_callback_request.ChannelFlowCallbackRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.channel_flow_callback_response.ChannelFlowCallbackResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.channel_flow_callback

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.channel_flow_callback.channel_flow_callback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.channel_flow_callback_request.ChannelFlowCallbackRequest = {}  # type: ignore[typeddict-item]
        input_["callback_id"] = callback_id
        input_["channel_arn"] = channel_arn
        if delete_resource is not None:
            input_["delete_resource"] = delete_resource
        input_["channel_message"] = channel_message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        name: "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName",
        client_request_token: "aws_sdk_chime_sdk_messaging.types.client_request_token.ClientRequestToken",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        mode: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_mode.ChannelMode"
        ] = None,
        privacy: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
        ] = None,
        metadata: Optional[
            "aws_sdk_chime_sdk_messaging.types.metadata.Metadata"
        ] = None,
        tags: Optional["aws_sdk_chime_sdk_messaging.types.tag_list.TagList"] = None,
        channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_id.ChannelId"
        ] = None,
        member_arns: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_member_arns.ChannelMemberArns"
        ] = None,
        moderator_arns: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_moderator_arns.ChannelModeratorArns"
        ] = None,
        elastic_channel_configuration: Optional[
            "aws_sdk_chime_sdk_messaging.types.elastic_channel_configuration.ElasticChannelConfiguration"
        ] = None,
        expiration_settings: Optional[
            "aws_sdk_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.create_channel_response.CreateChannelResponse":
        """<p>Creates a channel to which you can add users and send messages.</p> <p> <b>Restriction</b>: You can't change a channel's privacy.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            app_instance_arn: <p>The ARN of the channel request.</p>
            name: <p>The name of the channel.</p>
            mode: <p>The channel mode: <code>UNRESTRICTED</code> or <code>RESTRICTED</code>. Administrators, moderators, and channel members can add themselves and other members to unrestricted channels. Only administrators and moderators can add members to restricted channels.</p>
            privacy: <p>The channel's privacy level: <code>PUBLIC</code> or <code>PRIVATE</code>. Private channels aren't discoverable by users outside the channel. Public channels are discoverable by anyone in the <code>AppInstance</code>.</p>
            metadata: <p>The metadata of the creation request. Limited to 1KB and UTF-8.</p>
            client_request_token: <p>The client token for the request. An <code>Idempotency</code> token.</p>
            tags: <p>The tags for the creation request.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            channel_id: <p>An ID for the channel being created. If you do not specify an ID, a UUID will be created for the channel.</p>
            member_arns: <p>The ARNs of the channel members in the request.</p>
            moderator_arns: <p>The ARNs of the channel moderators in the request.</p>
            elastic_channel_configuration: <p>The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million users, excluding moderators.</p>
            expiration_settings: <p>Settings that control the interval after which the channel is automatically deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.create_channel_response.CreateChannelResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.create_channel_request.CreateChannelRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
        input_["name"] = name
        if mode is not None:
            input_["mode"] = mode
        if privacy is not None:
            input_["privacy"] = privacy
        if metadata is not None:
            input_["metadata"] = metadata
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        input_["chime_bearer"] = chime_bearer
        if channel_id is not None:
            input_["channel_id"] = channel_id
        if member_arns is not None:
            input_["member_arns"] = member_arns
        if moderator_arns is not None:
            input_["moderator_arns"] = moderator_arns
        if elastic_channel_configuration is not None:
            input_["elastic_channel_configuration"] = elastic_channel_configuration
        if expiration_settings is not None:
            input_["expiration_settings"] = expiration_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel_ban(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.create_channel_ban_response.CreateChannelBanResponse":
        """<p>Permanently bans a member from a channel. Moderators can't add banned members to a channel. To undo a ban, you first have to <code>DeleteChannelBan</code>, and then <code>CreateChannelMembership</code>. Bans are cleaned up when you delete users or channels.</p> <p>If you ban a user who is already part of a channel, that user is automatically kicked from the channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the ban request.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member being banned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.create_channel_ban_request.CreateChannelBanRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.create_channel_ban_response.CreateChannelBanResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel_ban

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel_ban.create_channel_ban(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.create_channel_ban_request.CreateChannelBanRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["member_arn"] = member_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel_flow(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        processors: "aws_sdk_chime_sdk_messaging.types.processor_list.ProcessorList",
        name: "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName",
        client_request_token: "aws_sdk_chime_sdk_messaging.types.client_request_token.ClientRequestToken",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        tags: Optional["aws_sdk_chime_sdk_messaging.types.tag_list.TagList"] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.create_channel_flow_response.CreateChannelFlowResponse":
        r"""<p>Creates a channel flow, a container for processors. Processors are AWS Lambda functions that perform actions on chat messages, such as stripping out profanity. You can associate channel flows with channels, and the processors in the channel flow then take action on all messages sent to that channel. This is a developer API.</p> <p>Channel flows process the following items:</p> <ol> <li> <p>New and updated messages</p> </li> <li> <p>Persistent and non-persistent messages</p> </li> <li> <p>The Standard message type</p> </li> </ol> <note> <p>Channel flows don't process Control or System messages. For more information about the message types provided by Chime SDK messaging, refer to <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/using-the-messaging-sdk.html#msg-types\">Message types</a> in the <i>Amazon Chime developer guide</i>.</p> </note>

        Args:
            app_instance_arn: <p>The ARN of the channel flow request.</p>
            processors: <p>Information about the processor Lambda functions.</p>
            name: <p>The name of the channel flow.</p>
            tags: <p>The tags for the creation request.</p>
            client_request_token: <p>The client token for the request. An Idempotency token.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.create_channel_flow_request.CreateChannelFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.create_channel_flow_response.CreateChannelFlowResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel_flow

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel_flow.create_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.create_channel_flow_request.CreateChannelFlowRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
        input_["processors"] = processors
        input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel_membership(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        type: "aws_sdk_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.create_channel_membership_response.CreateChannelMembershipResponse":
        """<p>Adds a member to a channel. The <code>InvitedBy</code> field in <code>ChannelMembership</code> is derived from the request header. A channel member can:</p> <ul> <li> <p>List messages</p> </li> <li> <p>Send messages</p> </li> <li> <p>Receive messages</p> </li> <li> <p>Edit their own messages</p> </li> <li> <p>Leave the channel</p> </li> </ul> <p>Privacy settings impact this action as follows:</p> <ul> <li> <p>Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.</p> </li> <li> <p>Private Channels: You must be a member to list or send messages.</p> </li> </ul> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUserArn</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel to which you're adding users.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member you want to add to the channel.</p>
            type: <p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned. This is only supported by moderators.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when creating membership in a SubChannel for a moderator in an elastic channel.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.create_channel_membership_request.CreateChannelMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.create_channel_membership_response.CreateChannelMembershipResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel_membership

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel_membership.create_channel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.create_channel_membership_request.CreateChannelMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["member_arn"] = member_arn
        input_["type"] = type
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def create_channel_moderator(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_moderator_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.create_channel_moderator_response.CreateChannelModeratorResponse":
        """<p>Creates a new <code>ChannelModerator</code>. A channel moderator can:</p> <ul> <li> <p>Add and remove other members of the channel.</p> </li> <li> <p>Add and remove other moderators of the channel.</p> </li> <li> <p>Add and remove user bans for the channel.</p> </li> <li> <p>Redact messages in the channel.</p> </li> <li> <p>List messages in the channel.</p> </li> </ul> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code>of the user that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_moderator_arn: <p>The <code>AppInstanceUserArn</code> of the moderator.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.create_channel_moderator_request.CreateChannelModeratorRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.create_channel_moderator_response.CreateChannelModeratorResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel_moderator

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.create_channel_moderator.create_channel_moderator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.create_channel_moderator_request.CreateChannelModeratorRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["channel_moderator_arn"] = channel_moderator_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Immediately makes a channel and its memberships inaccessible and marks them for deletion. This is an irreversible process.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUserArn</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel being deleted.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.delete_channel_request.DeleteChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel_ban(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Removes a member from a channel's ban list.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel from which the <code>AppInstanceUser</code> was banned.</p>
            member_arn: <p>The ARN of the <code>AppInstanceUser</code> that you want to reinstate.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.delete_channel_ban_request.DeleteChannelBanRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_ban

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_ban.delete_channel_ban(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.delete_channel_ban_request.DeleteChannelBanRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["member_arn"] = member_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel_flow(
        self,
        channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Deletes a channel flow, an irreversible process. This is a developer API.</p> <note> <p> This API works only when the channel flow is not associated with any channel. To get a list of all channels that a channel flow is associated with, use the <code>ListChannelsAssociatedWithChannelFlow</code> API. Use the <code>DisassociateChannelFlow</code> API to disassociate a channel flow from all channels. </p> </note>

        Args:
            channel_flow_arn: <p>The ARN of the channel flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.delete_channel_flow_request.DeleteChannelFlowRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_flow

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_flow.delete_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.delete_channel_flow_request.DeleteChannelFlowRequest = {}  # type: ignore[typeddict-item]
        input_["channel_flow_arn"] = channel_flow_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel_membership(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> None:
        """<p>Removes a member from a channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the <code>AppInstanceUserArn</code> of the user that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel from which you want to remove the user.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member that you're removing from the channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only for use by moderators.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.delete_channel_membership_request.DeleteChannelMembershipRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_membership

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_membership.delete_channel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.delete_channel_membership_request.DeleteChannelMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["member_arn"] = member_arn
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel_message(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> None:
        """<p>Deletes a channel message. Only admins can perform this action. Deletion makes messages inaccessible immediately. A background process deletes any revisions created by <code>UpdateChannelMessage</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            message_id: <p>The ID of the message being deleted.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when deleting messages in a SubChannel that the user belongs to.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.delete_channel_message_request.DeleteChannelMessageRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_message

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_message.delete_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.delete_channel_message_request.DeleteChannelMessageRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["message_id"] = message_id
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_channel_moderator(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_moderator_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Deletes a channel moderator.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_moderator_arn: <p>The <code>AppInstanceUserArn</code> of the moderator being deleted.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.delete_channel_moderator_request.DeleteChannelModeratorRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_moderator

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_channel_moderator.delete_channel_moderator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.delete_channel_moderator_request.DeleteChannelModeratorRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["channel_moderator_arn"] = channel_moderator_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete_messaging_streaming_configurations(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        r"""<p>Deletes the streaming configurations for an <code>AppInstance</code>. For more information, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\">Streaming messaging data</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>

        Args:
            app_instance_arn: <p>The ARN of the streaming configurations being deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.delete_messaging_streaming_configurations_request.DeleteMessagingStreamingConfigurationsRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_messaging_streaming_configurations

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.delete_messaging_streaming_configurations.delete_messaging_streaming_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.delete_messaging_streaming_configurations_request.DeleteMessagingStreamingConfigurationsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.describe_channel_response.DescribeChannelResponse":
        """<p>Returns the full details of a channel in an Amazon Chime <code>AppInstance</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.describe_channel_request.DescribeChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel.describe_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.describe_channel_request.DescribeChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel_ban(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.describe_channel_ban_response.DescribeChannelBanResponse":
        """<p>Returns the full details of a channel ban.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel from which the user is banned.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member being banned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.describe_channel_ban_request.DescribeChannelBanRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.describe_channel_ban_response.DescribeChannelBanResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_ban

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_ban.describe_channel_ban(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.describe_channel_ban_request.DescribeChannelBanRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["member_arn"] = member_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel_flow(
        self,
        channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.describe_channel_flow_response.DescribeChannelFlowResponse":
        """<p>Returns the full details of a channel flow in an Amazon Chime <code>AppInstance</code>. This is a developer API.</p>

        Args:
            channel_flow_arn: <p>The ARN of the channel flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.describe_channel_flow_request.DescribeChannelFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.describe_channel_flow_response.DescribeChannelFlowResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_flow

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_flow.describe_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.describe_channel_flow_request.DescribeChannelFlowRequest = {}  # type: ignore[typeddict-item]
        input_["channel_flow_arn"] = channel_flow_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel_membership(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.describe_channel_membership_response.DescribeChannelMembershipResponse":
        """<p>Returns the full details of a user's channel membership.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request. The response contains an <code>ElasticChannelConfiguration</code> object.</p> <note> <p>Only required to get a user’s SubChannel membership details.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.describe_channel_membership_request.DescribeChannelMembershipRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.describe_channel_membership_response.DescribeChannelMembershipResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_membership

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_membership.describe_channel_membership(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.describe_channel_membership_request.DescribeChannelMembershipRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["member_arn"] = member_arn
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel_membership_for_app_instance_user(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        app_instance_user_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_response.DescribeChannelMembershipForAppInstanceUserResponse":
        """<p> Returns the details of a channel based on the membership of the specified <code>AppInstanceUser</code> or <code>AppInstanceBot</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel to which the user belongs.</p>
            app_instance_user_arn: <p>The ARN of the user or bot in a channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_request.DescribeChannelMembershipForAppInstanceUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_response.DescribeChannelMembershipForAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_membership_for_app_instance_user

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_membership_for_app_instance_user.describe_channel_membership_for_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.describe_channel_membership_for_app_instance_user_request.DescribeChannelMembershipForAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["app_instance_user_arn"] = app_instance_user_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel_moderated_by_app_instance_user(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        app_instance_user_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse":
        """<p>Returns the full details of a channel moderated by the specified <code>AppInstanceUser</code> or <code>AppInstanceBot</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the moderated channel.</p>
            app_instance_user_arn: <p>The ARN of the user or bot in the moderated channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request.DescribeChannelModeratedByAppInstanceUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_response.DescribeChannelModeratedByAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_moderated_by_app_instance_user

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_moderated_by_app_instance_user.describe_channel_moderated_by_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.describe_channel_moderated_by_app_instance_user_request.DescribeChannelModeratedByAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["app_instance_user_arn"] = app_instance_user_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def describe_channel_moderator(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_moderator_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.describe_channel_moderator_response.DescribeChannelModeratorResponse":
        """<p>Returns the full details of a single ChannelModerator.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the <code>AppInstanceUserArn</code> of the user that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_moderator_arn: <p>The <code>AppInstanceUserArn</code> of the channel moderator.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.describe_channel_moderator_request.DescribeChannelModeratorRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.describe_channel_moderator_response.DescribeChannelModeratorResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_moderator

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.describe_channel_moderator.describe_channel_moderator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.describe_channel_moderator_request.DescribeChannelModeratorRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["channel_moderator_arn"] = channel_moderator_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def disassociate_channel_flow(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Disassociates a channel flow from all its channels. Once disassociated, all messages to that channel stop going through the channel flow processor.</p> <note> <p>Only administrators or channel moderators can disassociate a channel flow.</p> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            channel_flow_arn: <p>The ARN of the channel flow.</p>
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.disassociate_channel_flow_request.DisassociateChannelFlowRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.disassociate_channel_flow

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.disassociate_channel_flow.disassociate_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.disassociate_channel_flow_request.DisassociateChannelFlowRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["channel_flow_arn"] = channel_flow_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_channel_membership_preferences(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.get_channel_membership_preferences_response.GetChannelMembershipPreferencesResponse":
        """<p>Gets the membership preferences of an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> for the specified channel. A user or a bot must be a member of the channel and own the membership in order to retrieve membership preferences. Users or bots in the <code>AppInstanceAdmin</code> and channel moderator roles can't retrieve preferences for other users or bots. Banned users or bots can't retrieve membership preferences for the channel from which they are banned.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            member_arn: <p>The <code>AppInstanceUserArn</code> of the member retrieving the preferences.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.get_channel_membership_preferences_request.GetChannelMembershipPreferencesRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.get_channel_membership_preferences_response.GetChannelMembershipPreferencesResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_channel_membership_preferences

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_channel_membership_preferences.get_channel_membership_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.get_channel_membership_preferences_request.GetChannelMembershipPreferencesRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["member_arn"] = member_arn
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_channel_message(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.get_channel_message_response.GetChannelMessageResponse":
        """<p>Gets the full details of a channel message.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            message_id: <p>The ID of the message.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting messages in a SubChannel that the user belongs to.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.get_channel_message_request.GetChannelMessageRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.get_channel_message_response.GetChannelMessageResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_channel_message

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_channel_message.get_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.get_channel_message_request.GetChannelMessageRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["message_id"] = message_id
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_channel_message_status(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.get_channel_message_status_response.GetChannelMessageStatusResponse":
        """<p>Gets message status for a specified <code>messageId</code>. Use this API to determine the intermediate status of messages going through channel flow processing. The API provides an alternative to retrieving message status if the event was not received because a client wasn't connected to a websocket. </p> <p>Messages can have any one of these statuses.</p> <dl> <dt>SENT</dt> <dd> <p>Message processed successfully</p> </dd> <dt>PENDING</dt> <dd> <p>Ongoing processing</p> </dd> <dt>FAILED</dt> <dd> <p>Processing failed</p> </dd> <dt>DENIED</dt> <dd> <p>Message denied by the processor</p> </dd> </dl> <note> <ul> <li> <p>This API does not return statuses for denied messages, because we don't store them once the processor denies them. </p> </li> <li> <p>Only the message sender can invoke this API.</p> </li> <li> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </li> </ul> </note>

        Args:
            channel_arn: <p>The ARN of the channel</p>
            message_id: <p>The ID of the message.</p>
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting message status in a SubChannel that the user belongs to.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.get_channel_message_status_request.GetChannelMessageStatusRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.get_channel_message_status_response.GetChannelMessageStatusResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_channel_message_status

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_channel_message_status.get_channel_message_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.get_channel_message_status_request.GetChannelMessageStatusRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["message_id"] = message_id
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_messaging_session_endpoint(
        self,
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        network_type: Optional[
            "aws_sdk_chime_sdk_messaging.types.network_type.NetworkType"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.get_messaging_session_endpoint_response.GetMessagingSessionEndpointResponse":
        """<p>The details of the endpoint for the messaging session.</p>

        Args:
            network_type: <p>The type of network for the messaging session endpoint. Either IPv4 only or dual-stack (IPv4 and IPv6).</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.get_messaging_session_endpoint_request.GetMessagingSessionEndpointRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.get_messaging_session_endpoint_response.GetMessagingSessionEndpointResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_messaging_session_endpoint

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_messaging_session_endpoint.get_messaging_session_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.get_messaging_session_endpoint_request.GetMessagingSessionEndpointRequest = {}  # type: ignore[typeddict-item]
        if network_type is not None:
            input_["network_type"] = network_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_messaging_streaming_configurations(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.get_messaging_streaming_configurations_response.GetMessagingStreamingConfigurationsResponse":
        r"""<p>Retrieves the data streaming configuration for an <code>AppInstance</code>. For more information, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\">Streaming messaging data</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>

        Args:
            app_instance_arn: <p>The ARN of the streaming configurations.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.get_messaging_streaming_configurations_request.GetMessagingStreamingConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.get_messaging_streaming_configurations_response.GetMessagingStreamingConfigurationsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_messaging_streaming_configurations

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.get_messaging_streaming_configurations.get_messaging_streaming_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.get_messaging_streaming_configurations_request.GetMessagingStreamingConfigurationsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channel_bans(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_channel_bans_response.ListChannelBansResponse":
        """<p>Lists all the users and bots banned from a particular channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            max_results: <p>The maximum number of bans that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested bans are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channel_bans_request.ListChannelBansRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channel_bans_response.ListChannelBansResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_bans

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_bans.list_channel_bans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channel_bans_request.ListChannelBansRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channel_flows(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_channel_flows_response.ListChannelFlowsResponse":
        """<p>Returns a paginated lists of all the channel flows created under a single Chime. This is a developer API.</p>

        Args:
            app_instance_arn: <p>The ARN of the app instance.</p>
            max_results: <p>The maximum number of channel flows that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested channel flows are returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channel_flows_request.ListChannelFlowsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channel_flows_response.ListChannelFlowsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_flows

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_flows.list_channel_flows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channel_flows_request.ListChannelFlowsRequest = {}  # type: ignore[typeddict-item]
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

    def list_channel_memberships(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        type: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
        ] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_channel_memberships_response.ListChannelMembershipsResponse":
        r"""<p>Lists all channel memberships in a channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note> <p>If you want to list the channels to which a specific app instance user belongs, see the <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html\">ListChannelMembershipsForAppInstanceUser</a> API.</p>

        Args:
            channel_arn: <p>The maximum number of channel memberships that you want returned.</p>
            type: <p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are returned as part of <code>ListChannelMemberships</code> if no type is specified. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>.</p>
            max_results: <p>The maximum number of channel memberships that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested channel memberships are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing a user's memberships in a particular sub-channel of an elastic channel.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channel_memberships_request.ListChannelMembershipsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channel_memberships_response.ListChannelMembershipsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_memberships

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_memberships.list_channel_memberships(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channel_memberships_request.ListChannelMembershipsRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if type is not None:
            input_["type"] = type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channel_memberships_for_app_instance_user(
        self,
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        app_instance_user_arn: Optional[
            "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_response.ListChannelMembershipsForAppInstanceUserResponse":
        """<p> Lists all channels that an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> is a part of. Only an <code>AppInstanceAdmin</code> can call the API with a user ARN that is not their own. </p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            app_instance_user_arn: <p>The ARN of the user or bot.</p>
            max_results: <p>The maximum number of users that you want returned.</p>
            next_token: <p>The token returned from previous API requests until the number of channel memberships is reached.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_request.ListChannelMembershipsForAppInstanceUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_response.ListChannelMembershipsForAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_memberships_for_app_instance_user

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_memberships_for_app_instance_user.list_channel_memberships_for_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channel_memberships_for_app_instance_user_request.ListChannelMembershipsForAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        if app_instance_user_arn is not None:
            input_["app_instance_user_arn"] = app_instance_user_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channel_messages(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sort_order: Optional[
            "aws_sdk_chime_sdk_messaging.types.sort_order.SortOrder"
        ] = None,
        not_before: Optional[
            "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
        ] = None,
        not_after: Optional[
            "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
        ] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_channel_messages_response.ListChannelMessagesResponse":
        """<p>List all the messages in a channel. Returns a paginated list of <code>ChannelMessages</code>. By default, sorted by creation timestamp in descending order.</p> <note> <p>Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.</p> <p>Also, the <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            sort_order: <p>The order in which you want messages sorted. Default is Descending, based on time created.</p>
            not_before: <p>The initial or starting time stamp for your requested messages.</p>
            not_after: <p>The final or ending time stamp for your requested messages.</p>
            max_results: <p>The maximum number of messages that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested messages are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing the messages in a SubChannel that the user belongs to.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channel_messages_request.ListChannelMessagesRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channel_messages_response.ListChannelMessagesResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_messages

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_messages.list_channel_messages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channel_messages_request.ListChannelMessagesRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if not_before is not None:
            input_["not_before"] = not_before
        if not_after is not None:
            input_["not_after"] = not_after
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channel_moderators(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_channel_moderators_response.ListChannelModeratorsResponse":
        """<p>Lists all the moderators for a channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            max_results: <p>The maximum number of moderators that you want returned.</p>
            next_token: <p>The token passed by previous API calls until all requested moderators are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channel_moderators_request.ListChannelModeratorsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channel_moderators_response.ListChannelModeratorsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_moderators

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channel_moderators.list_channel_moderators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channel_moderators_request.ListChannelModeratorsRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channels(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        privacy: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_privacy.ChannelPrivacy"
        ] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> (
        "aws_sdk_chime_sdk_messaging.types.list_channels_response.ListChannelsResponse"
    ):
        r"""<p>Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.</p> <p class=\"title\"> <b>Functionality & restrictions</b> </p> <ul> <li> <p>Use privacy = <code>PUBLIC</code> to retrieve all public channels in the account.</p> </li> <li> <p>Only an <code>AppInstanceAdmin</code> can set privacy = <code>PRIVATE</code> to list the private channels in an account.</p> </li> </ul> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            app_instance_arn: <p>The ARN of the <code>AppInstance</code>.</p>
            privacy: <p>The privacy setting. <code>PUBLIC</code> retrieves all the public channels. <code>PRIVATE</code> retrieves private channels. Only an <code>AppInstanceAdmin</code> can retrieve private channels. </p>
            max_results: <p>The maximum number of channels that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested channels are returned.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channels_response.ListChannelsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channels

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channels_request.ListChannelsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
        if privacy is not None:
            input_["privacy"] = privacy
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_channels_associated_with_channel_flow(
        self,
        channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_response.ListChannelsAssociatedWithChannelFlowResponse":
        """<p>Lists all channels associated with a specified channel flow. You can associate a channel flow with multiple channels, but you can only associate a channel with one channel flow. This is a developer API.</p>

        Args:
            channel_flow_arn: <p>The ARN of the channel flow.</p>
            max_results: <p>The maximum number of channels that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested channels are returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_request.ListChannelsAssociatedWithChannelFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_response.ListChannelsAssociatedWithChannelFlowResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channels_associated_with_channel_flow

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channels_associated_with_channel_flow.list_channels_associated_with_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channels_associated_with_channel_flow_request.ListChannelsAssociatedWithChannelFlowRequest = {}  # type: ignore[typeddict-item]
        input_["channel_flow_arn"] = channel_flow_arn
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

    def list_channels_moderated_by_app_instance_user(
        self,
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        app_instance_user_arn: Optional[
            "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_response.ListChannelsModeratedByAppInstanceUserResponse":
        """<p>A list of the channels moderated by an <code>AppInstanceUser</code>.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            app_instance_user_arn: <p>The ARN of the user or bot in the moderated channel.</p>
            max_results: <p>The maximum number of channels in the request.</p>
            next_token: <p>The token returned from previous API requests until the number of channels moderated by the user is reached.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_request.ListChannelsModeratedByAppInstanceUserRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_response.ListChannelsModeratedByAppInstanceUserResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channels_moderated_by_app_instance_user

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_channels_moderated_by_app_instance_user.list_channels_moderated_by_app_instance_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_channels_moderated_by_app_instance_user_request.ListChannelsModeratedByAppInstanceUserRequest = {}  # type: ignore[typeddict-item]
        if app_instance_user_arn is not None:
            input_["app_instance_user_arn"] = app_instance_user_arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list_sub_channels(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_sub_channels_response.ListSubChannelsResponse":
        """<p>Lists all the SubChannels in an elastic channel when given a channel ID. Available only to the app instance admins and channel moderators of elastic channels.</p>

        Args:
            channel_arn: <p>The ARN of elastic channel.</p>
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>
            max_results: <p>The maximum number of sub-channels that you want to return.</p>
            next_token: <p>The token passed by previous API calls until all requested sub-channels are returned.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_sub_channels_request.ListSubChannelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_sub_channels_response.ListSubChannelsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_sub_channels

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_sub_channels.list_sub_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_sub_channels_request.ListSubChannelsRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["chime_bearer"] = chime_bearer
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
        resource_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags applied to an Amazon Chime SDK messaging resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_tags_for_resource

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_channel_expiration_settings(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        chime_bearer: Optional[
            "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        expiration_settings: Optional[
            "aws_sdk_chime_sdk_messaging.types.expiration_settings.ExpirationSettings"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.put_channel_expiration_settings_response.PutChannelExpirationSettingsResponse":
        """<p>Sets the number of days before the channel is automatically deleted.</p> <note> <ul> <li> <p>A background process deletes expired channels within 6 hours of expiration. Actual deletion times may vary.</p> </li> <li> <p>Expired channels that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.</p> </li> <li> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </li> </ul> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            expiration_settings: <p>Settings that control the interval after which a channel is deleted.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.put_channel_expiration_settings_request.PutChannelExpirationSettingsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.put_channel_expiration_settings_response.PutChannelExpirationSettingsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.put_channel_expiration_settings

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.put_channel_expiration_settings.put_channel_expiration_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.put_channel_expiration_settings_request.PutChannelExpirationSettingsRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if chime_bearer is not None:
            input_["chime_bearer"] = chime_bearer
        if expiration_settings is not None:
            input_["expiration_settings"] = expiration_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_channel_membership_preferences(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        preferences: "aws_sdk_chime_sdk_messaging.types.channel_membership_preferences.ChannelMembershipPreferences",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.put_channel_membership_preferences_response.PutChannelMembershipPreferencesResponse":
        """<p>Sets the membership preferences of an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> for the specified channel. The user or bot must be a member of the channel. Only the user or bot who owns the membership can set preferences. Users or bots in the <code>AppInstanceAdmin</code> and channel moderator roles can't set preferences for other users. Banned users or bots can't set membership preferences for the channel from which they are banned.</p> <note> <p>The x-amz-chime-bearer request header is mandatory. Use the ARN of an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            member_arn: <p>The ARN of the member setting the preferences.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            preferences: <p>The channel membership preferences of an <code>AppInstanceUser</code> .</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.put_channel_membership_preferences_request.PutChannelMembershipPreferencesRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.put_channel_membership_preferences_response.PutChannelMembershipPreferencesResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.put_channel_membership_preferences

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.put_channel_membership_preferences.put_channel_membership_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.put_channel_membership_preferences_request.PutChannelMembershipPreferencesRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["member_arn"] = member_arn
        input_["chime_bearer"] = chime_bearer
        input_["preferences"] = preferences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def put_messaging_streaming_configurations(
        self,
        app_instance_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        streaming_configurations: "aws_sdk_chime_sdk_messaging.types.streaming_configuration_list.StreamingConfigurationList",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.put_messaging_streaming_configurations_response.PutMessagingStreamingConfigurationsResponse":
        r"""<p>Sets the data streaming configuration for an <code>AppInstance</code>. For more information, see <a href=\"https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\">Streaming messaging data</a> in the <i>Amazon Chime SDK Developer Guide</i>.</p>

        Args:
            app_instance_arn: <p>The ARN of the streaming configuration.</p>
            streaming_configurations: <p>The streaming configurations.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.put_messaging_streaming_configurations_request.PutMessagingStreamingConfigurationsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.put_messaging_streaming_configurations_response.PutMessagingStreamingConfigurationsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.put_messaging_streaming_configurations

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.put_messaging_streaming_configurations.put_messaging_streaming_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.put_messaging_streaming_configurations_request.PutMessagingStreamingConfigurationsRequest = {}  # type: ignore[typeddict-item]
        input_["app_instance_arn"] = app_instance_arn
        input_["streaming_configurations"] = streaming_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def redact_channel_message(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.redact_channel_message_response.RedactChannelMessageResponse":
        """<p>Redacts message content and metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel containing the messages that you want to redact.</p>
            message_id: <p>The ID of the message being redacted.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.redact_channel_message_request.RedactChannelMessageRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.redact_channel_message_response.RedactChannelMessageResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.redact_channel_message

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.redact_channel_message.redact_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.redact_channel_message_request.RedactChannelMessageRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["message_id"] = message_id
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def search_channels(
        self,
        fields: "aws_sdk_chime_sdk_messaging.types.search_fields.SearchFields",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        chime_bearer: Optional[
            "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
        ] = None,
        max_results: Optional[
            "aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "aws_sdk_chime_sdk_messaging.types.next_token.NextToken"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.search_channels_response.SearchChannelsResponse":
        """<p>Allows the <code>ChimeBearer</code> to search channels by channel members. Users or bots can search across the channels that they belong to. Users in the <code>AppInstanceAdmin</code> role can search across all channels.</p> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> <note> <p>This operation isn't supported for <code>AppInstanceUsers</code> with a large number of memberships.</p> </note>

        Args:
            chime_bearer: <p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>
            fields: <p>A list of the <code>Field</code> objects in the channel being searched.</p>
            max_results: <p>The maximum number of channels that you want returned.</p>
            next_token: <p>The token returned from previous API requests until the number of channels is reached.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.search_channels_request.SearchChannelsRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.search_channels_response.SearchChannelsResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.search_channels

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.search_channels.search_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.search_channels_request.SearchChannelsRequest = {}  # type: ignore[typeddict-item]
        if chime_bearer is not None:
            input_["chime_bearer"] = chime_bearer
        input_["fields"] = fields
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

    def send_channel_message(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        content: "aws_sdk_chime_sdk_messaging.types.non_empty_content.NonEmptyContent",
        type: "aws_sdk_chime_sdk_messaging.types.channel_message_type.ChannelMessageType",
        persistence: "aws_sdk_chime_sdk_messaging.types.channel_message_persistence_type.ChannelMessagePersistenceType",
        client_request_token: "aws_sdk_chime_sdk_messaging.types.client_request_token.ClientRequestToken",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        metadata: Optional[
            "aws_sdk_chime_sdk_messaging.types.metadata.Metadata"
        ] = None,
        push_notification: Optional[
            "aws_sdk_chime_sdk_messaging.types.push_notification_configuration.PushNotificationConfiguration"
        ] = None,
        message_attributes: Optional[
            "aws_sdk_chime_sdk_messaging.types.message_attribute_map.MessageAttributeMap"
        ] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
        content_type: Optional[
            "aws_sdk_chime_sdk_messaging.types.content_type.ContentType"
        ] = None,
        target: Optional[
            "aws_sdk_chime_sdk_messaging.types.target_list.TargetList"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.send_channel_message_response.SendChannelMessageResponse":
        """<p>Sends a message to a particular channel that the member is a part of.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> <p>Also, <code>STANDARD</code> messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.</p> <p> <code>CONTROL</code> messages are limited to 30 bytes and do not contain metadata.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            content: <p>The content of the channel message.</p>
            type: <p>The type of message, <code>STANDARD</code> or <code>CONTROL</code>.</p> <p> <code>STANDARD</code> messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.</p> <p> <code>CONTROL</code> messages are limited to 30 bytes and do not contain metadata.</p>
            persistence: <p>Boolean that controls whether the message is persisted on the back end. Required.</p>
            metadata: <p>The optional metadata for each message.</p>
            client_request_token: <p>The <code>Idempotency</code> token for each client request.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            push_notification: <p>The push notification configuration of the message.</p>
            message_attributes: <p>The attributes for the message, used for message filtering along with a <code>FilterRule</code> defined in the <code>PushNotificationPreferences</code>.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p>
            content_type: <p>The content type of the channel message.</p>
            target: <p>The target of a message. Must be a member of the channel, such as another user, a bot, or the sender. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see. </p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.send_channel_message_request.SendChannelMessageRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.send_channel_message_response.SendChannelMessageResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.send_channel_message

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.send_channel_message.send_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.send_channel_message_request.SendChannelMessageRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["content"] = content
        input_["type"] = type
        input_["persistence"] = persistence
        if metadata is not None:
            input_["metadata"] = metadata
        input_["client_request_token"] = client_request_token
        input_["chime_bearer"] = chime_bearer
        if push_notification is not None:
            input_["push_notification"] = push_notification
        if message_attributes is not None:
            input_["message_attributes"] = message_attributes
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id
        if content_type is not None:
            input_["content_type"] = content_type
        if target is not None:
            input_["target"] = target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def tag_resource(
        self,
        resource_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        tags: "aws_sdk_chime_sdk_messaging.types.tag_list.TagList",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Applies the specified tags to the specified Amazon Chime SDK messaging resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tags: <p>The tag key-value pairs.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.tag_resource

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        tag_keys: "aws_sdk_chime_sdk_messaging.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> None:
        """<p>Removes the specified tags from the specified Amazon Chime SDK messaging resource.</p>

        Args:
            resource_arn: <p>The resource ARN.</p>
            tag_keys: <p>The tag keys.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.untag_resource

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        name: Optional[
            "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
        ] = None,
        mode: Optional[
            "aws_sdk_chime_sdk_messaging.types.channel_mode.ChannelMode"
        ] = None,
        metadata: Optional[
            "aws_sdk_chime_sdk_messaging.types.metadata.Metadata"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.update_channel_response.UpdateChannelResponse":
        """<p>Update a channel's attributes.</p> <p> <b>Restriction</b>: You can't change a channel's privacy. </p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            name: <p>The name of the channel.</p>
            mode: <p>The mode of the update request.</p>
            metadata: <p>The metadata for the update request.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.update_channel_response.UpdateChannelResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.update_channel

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.update_channel_request.UpdateChannelRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        if name is not None:
            input_["name"] = name
        if mode is not None:
            input_["mode"] = mode
        if metadata is not None:
            input_["metadata"] = metadata
        input_["chime_bearer"] = chime_bearer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel_flow(
        self,
        channel_flow_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        processors: "aws_sdk_chime_sdk_messaging.types.processor_list.ProcessorList",
        name: "aws_sdk_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.update_channel_flow_response.UpdateChannelFlowResponse":
        """<p>Updates channel flow attributes. This is a developer API.</p>

        Args:
            channel_flow_arn: <p>The ARN of the channel flow.</p>
            processors: <p>Information about the processor Lambda functions </p>
            name: <p>The name of the channel flow.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.update_channel_flow_request.UpdateChannelFlowRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.update_channel_flow_response.UpdateChannelFlowResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.update_channel_flow

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.update_channel_flow.update_channel_flow(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.update_channel_flow_request.UpdateChannelFlowRequest = {}  # type: ignore[typeddict-item]
        input_["channel_flow_arn"] = channel_flow_arn
        input_["processors"] = processors
        input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel_message(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        message_id: "aws_sdk_chime_sdk_messaging.types.message_id.MessageId",
        content: "aws_sdk_chime_sdk_messaging.types.non_empty_content.NonEmptyContent",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
        metadata: Optional[
            "aws_sdk_chime_sdk_messaging.types.metadata.Metadata"
        ] = None,
        sub_channel_id: Optional[
            "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
        ] = None,
        content_type: Optional[
            "aws_sdk_chime_sdk_messaging.types.content_type.ContentType"
        ] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.update_channel_message_response.UpdateChannelMessageResponse":
        """<p>Updates the content of a message.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            message_id: <p>The ID string of the message being updated.</p>
            content: <p>The content of the channel message. </p>
            metadata: <p>The metadata of the message being updated.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
            sub_channel_id: <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when updating messages in a SubChannel that the user belongs to.</p> </note>
            content_type: <p>The content type of the channel message.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.update_channel_message_request.UpdateChannelMessageRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.update_channel_message_response.UpdateChannelMessageResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.update_channel_message

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.update_channel_message.update_channel_message(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.update_channel_message_request.UpdateChannelMessageRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["message_id"] = message_id
        input_["content"] = content
        if metadata is not None:
            input_["metadata"] = metadata
        input_["chime_bearer"] = chime_bearer
        if sub_channel_id is not None:
            input_["sub_channel_id"] = sub_channel_id
        if content_type is not None:
            input_["content_type"] = content_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update_channel_read_marker(
        self,
        channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn",
        *,
        config_overrides: Optional[ChimeSDKMessagingClientConfig] = None,
    ) -> "aws_sdk_chime_sdk_messaging.types.update_channel_read_marker_response.UpdateChannelReadMarkerResponse":
        """<p>The details of the time when a user last read messages in a channel.</p> <note> <p>The <code>x-amz-chime-bearer</code> request header is mandatory. Use the ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call as the value in the header.</p> </note>

        Args:
            channel_arn: <p>The ARN of the channel.</p>
            chime_bearer: <p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_chime_sdk_messaging.types.update_channel_read_marker_request.UpdateChannelReadMarkerRequest]",
        ) -> OperationResponse[
            "aws_sdk_chime_sdk_messaging.types.update_channel_read_marker_response.UpdateChannelReadMarkerResponse"
        ]:
            import aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.update_channel_read_marker

            output, http_response = (
                aws_sdk_chime_sdk_messaging._operations.chime_messaging_service.update_channel_read_marker.update_channel_read_marker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chime_sdk_messaging.types.update_channel_read_marker_request.UpdateChannelReadMarkerRequest = {}  # type: ignore[typeddict-item]
        input_["channel_arn"] = channel_arn
        input_["chime_bearer"] = chime_bearer

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
