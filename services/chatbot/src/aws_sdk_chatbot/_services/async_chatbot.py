"""Generated from Smithy shape ``com.amazonaws.chatbot#WheatleyOrchestration_20171011``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional, TypedDict

from typing_extensions import Self
from zapros import AsyncBaseHandler, AsyncClient

import aws_sdk_chatbot._auth._signers
import aws_sdk_chatbot._auth._sigv4
from aws_sdk_chatbot._auth._identity import Credentials
from aws_sdk_chatbot._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from aws_sdk_chatbot._auth._zapros_handler import AuthMiddleware
from aws_sdk_chatbot._pagination import resolve_path as _resolve_path
from aws_sdk_chatbot._resources.wheatley_orchestration_20171011.custom_action_resource import (
    AsyncCustomActionResource,
)
from aws_sdk_chatbot._services._aws_config import aaws_config
from aws_sdk_chatbot._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.amazon_resource_name
    import aws_sdk_chatbot.types.arn
    import aws_sdk_chatbot.types.associate_to_configuration_request
    import aws_sdk_chatbot.types.associate_to_configuration_result
    import aws_sdk_chatbot.types.association_listing
    import aws_sdk_chatbot.types.boolean_account_preference
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.chime_webhook_configuration
    import aws_sdk_chatbot.types.chime_webhook_description
    import aws_sdk_chatbot.types.chime_webhook_url
    import aws_sdk_chatbot.types.configuration_name
    import aws_sdk_chatbot.types.configured_team
    import aws_sdk_chatbot.types.create_chime_webhook_configuration_request
    import aws_sdk_chatbot.types.create_chime_webhook_configuration_result
    import aws_sdk_chatbot.types.create_slack_channel_configuration_request
    import aws_sdk_chatbot.types.create_slack_channel_configuration_result
    import aws_sdk_chatbot.types.create_teams_channel_configuration_request
    import aws_sdk_chatbot.types.create_teams_channel_configuration_result
    import aws_sdk_chatbot.types.customer_cw_log_level
    import aws_sdk_chatbot.types.delete_chime_webhook_configuration_request
    import aws_sdk_chatbot.types.delete_chime_webhook_configuration_result
    import aws_sdk_chatbot.types.delete_microsoft_teams_user_identity_request
    import aws_sdk_chatbot.types.delete_microsoft_teams_user_identity_result
    import aws_sdk_chatbot.types.delete_slack_channel_configuration_request
    import aws_sdk_chatbot.types.delete_slack_channel_configuration_result
    import aws_sdk_chatbot.types.delete_slack_user_identity_request
    import aws_sdk_chatbot.types.delete_slack_user_identity_result
    import aws_sdk_chatbot.types.delete_slack_workspace_authorization_request
    import aws_sdk_chatbot.types.delete_slack_workspace_authorization_result
    import aws_sdk_chatbot.types.delete_teams_channel_configuration_request
    import aws_sdk_chatbot.types.delete_teams_channel_configuration_result
    import aws_sdk_chatbot.types.delete_teams_configured_team_request
    import aws_sdk_chatbot.types.delete_teams_configured_team_result
    import aws_sdk_chatbot.types.describe_chime_webhook_configurations_request
    import aws_sdk_chatbot.types.describe_chime_webhook_configurations_result
    import aws_sdk_chatbot.types.describe_slack_channel_configurations_request
    import aws_sdk_chatbot.types.describe_slack_channel_configurations_result
    import aws_sdk_chatbot.types.describe_slack_user_identities_request
    import aws_sdk_chatbot.types.describe_slack_user_identities_result
    import aws_sdk_chatbot.types.describe_slack_workspaces_request
    import aws_sdk_chatbot.types.describe_slack_workspaces_result
    import aws_sdk_chatbot.types.disassociate_from_configuration_request
    import aws_sdk_chatbot.types.disassociate_from_configuration_result
    import aws_sdk_chatbot.types.get_account_preferences_request
    import aws_sdk_chatbot.types.get_account_preferences_result
    import aws_sdk_chatbot.types.get_teams_channel_configuration_request
    import aws_sdk_chatbot.types.get_teams_channel_configuration_result
    import aws_sdk_chatbot.types.guardrail_policy_arn_list
    import aws_sdk_chatbot.types.list_associations_request
    import aws_sdk_chatbot.types.list_associations_result
    import aws_sdk_chatbot.types.list_microsoft_teams_configured_teams_request
    import aws_sdk_chatbot.types.list_microsoft_teams_configured_teams_result
    import aws_sdk_chatbot.types.list_microsoft_teams_user_identities_request
    import aws_sdk_chatbot.types.list_microsoft_teams_user_identities_result
    import aws_sdk_chatbot.types.list_tags_for_resource_request
    import aws_sdk_chatbot.types.list_tags_for_resource_response
    import aws_sdk_chatbot.types.list_teams_channel_configurations_request
    import aws_sdk_chatbot.types.list_teams_channel_configurations_result
    import aws_sdk_chatbot.types.max_results
    import aws_sdk_chatbot.types.pagination_token
    import aws_sdk_chatbot.types.resource_identifier
    import aws_sdk_chatbot.types.slack_channel_configuration
    import aws_sdk_chatbot.types.slack_channel_display_name
    import aws_sdk_chatbot.types.slack_channel_id
    import aws_sdk_chatbot.types.slack_team_id
    import aws_sdk_chatbot.types.slack_user_id
    import aws_sdk_chatbot.types.slack_user_identity
    import aws_sdk_chatbot.types.slack_workspace
    import aws_sdk_chatbot.types.sns_topic_arn_list
    import aws_sdk_chatbot.types.string
    import aws_sdk_chatbot.types.tag_key_list
    import aws_sdk_chatbot.types.tag_list
    import aws_sdk_chatbot.types.tag_resource_request
    import aws_sdk_chatbot.types.tag_resource_response
    import aws_sdk_chatbot.types.tags
    import aws_sdk_chatbot.types.team_name
    import aws_sdk_chatbot.types.teams_channel_configuration
    import aws_sdk_chatbot.types.teams_channel_id
    import aws_sdk_chatbot.types.teams_channel_name
    import aws_sdk_chatbot.types.teams_user_identity
    import aws_sdk_chatbot.types.untag_resource_request
    import aws_sdk_chatbot.types.untag_resource_response
    import aws_sdk_chatbot.types.update_account_preferences_request
    import aws_sdk_chatbot.types.update_account_preferences_result
    import aws_sdk_chatbot.types.update_chime_webhook_configuration_request
    import aws_sdk_chatbot.types.update_chime_webhook_configuration_result
    import aws_sdk_chatbot.types.update_slack_channel_configuration_request
    import aws_sdk_chatbot.types.update_slack_channel_configuration_result
    import aws_sdk_chatbot.types.update_teams_channel_configuration_request
    import aws_sdk_chatbot.types.update_teams_channel_configuration_result
    import aws_sdk_chatbot.types.uuid


class AsyncchatbotClientConfig(TypedDict, total=False):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncchatbotClient:
    """A client for the ``chatbot`` service.

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
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        self._config = AsyncchatbotClientConfig(
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
        self.custom_action_resource = AsyncCustomActionResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncchatbotClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncchatbotClientConfig = config_overrides or {}
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

    async def associate_to_configuration(
        self,
        resource: "aws_sdk_chatbot.types.resource_identifier.ResourceIdentifier",
        chat_configuration: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.associate_to_configuration_result.AssociateToConfigurationResult":
        """<p>Links a resource (for example, a custom action) to a channel configuration.</p>

        Args:
            resource: <p>The resource Amazon Resource Name (ARN) to link.</p>
            chat_configuration: <p>The channel configuration to associate with the resource.</p>

        Examples:
            Associate a custom action to a configuration
            Associate a custom action to a channel configuration, allowing it to be used in that channel

            >>> await client.associate_to_configuration(resource='arn:aws:chatbot::1234567890:custom-action/my-custom-action', chat_configuration='arn:aws:chatbot::1234567890:chat-configuration/slack-channel/my-channel')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.associate_to_configuration_request.AssociateToConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.associate_to_configuration_result.AssociateToConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.associate_to_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.associate_to_configuration.async_associate_to_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.associate_to_configuration_request.AssociateToConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["chat_configuration"] = chat_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_chime_webhook_configuration(
        self,
        webhook_description: "aws_sdk_chatbot.types.chime_webhook_description.ChimeWebhookDescription",
        webhook_url: "aws_sdk_chatbot.types.chime_webhook_url.ChimeWebhookUrl",
        sns_topic_arns: "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList",
        iam_role_arn: "aws_sdk_chatbot.types.arn.Arn",
        configuration_name: "aws_sdk_chatbot.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        logging_level: Optional[
            "aws_sdk_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        tags: Optional["aws_sdk_chatbot.types.tags.Tags"] = None,
    ) -> "aws_sdk_chatbot.types.create_chime_webhook_configuration_result.CreateChimeWebhookConfigurationResult":
        r"""<p>Creates an AWS Chatbot configuration for Amazon Chime.</p>

        Args:
            webhook_description: <p>A description of the webhook. We recommend using the convention <code>RoomName/WebhookName</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html\">Tutorial: Get started with Amazon Chime</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            webhook_url: <p>The URL for the Amazon Chime webhook.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            configuration_name: <p>The name of the configuration.</p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.create_chime_webhook_configuration_request.CreateChimeWebhookConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.create_chime_webhook_configuration_result.CreateChimeWebhookConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.create_chime_webhook_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.create_chime_webhook_configuration.async_create_chime_webhook_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.create_chime_webhook_configuration_request.CreateChimeWebhookConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["webhook_description"] = webhook_description
        input_["webhook_url"] = webhook_url
        input_["sns_topic_arns"] = sns_topic_arns
        input_["iam_role_arn"] = iam_role_arn
        input_["configuration_name"] = configuration_name
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_microsoft_teams_channel_configuration(
        self,
        channel_id: "aws_sdk_chatbot.types.teams_channel_id.TeamsChannelId",
        team_id: "aws_sdk_chatbot.types.uuid.UUID",
        tenant_id: "aws_sdk_chatbot.types.uuid.UUID",
        iam_role_arn: "aws_sdk_chatbot.types.arn.Arn",
        configuration_name: "aws_sdk_chatbot.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        channel_name: Optional[
            "aws_sdk_chatbot.types.teams_channel_name.TeamsChannelName"
        ] = None,
        team_name: Optional["aws_sdk_chatbot.types.team_name.TeamName"] = None,
        sns_topic_arns: Optional[
            "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        logging_level: Optional[
            "aws_sdk_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        guardrail_policy_arns: Optional[
            "aws_sdk_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
        ] = None,
        user_authorization_required: Optional[
            "aws_sdk_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
        tags: Optional["aws_sdk_chatbot.types.tags.Tags"] = None,
    ) -> "aws_sdk_chatbot.types.create_teams_channel_configuration_result.CreateTeamsChannelConfigurationResult":
        r"""<p>Creates an AWS Chatbot configuration for Microsoft Teams.</p>

        Args:
            channel_id: <p>The ID of the Microsoft Teams channel.</p>
            channel_name: <p>The name of the Microsoft Teams channel.</p>
            team_id: <p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup\">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            team_name: <p>The name of the Microsoft Teams Team.</p>
            tenant_id: <p>The ID of the Microsoft Teams tenant.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            configuration_name: <p>The name of the configuration.</p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            guardrail_policy_arns: <p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.create_teams_channel_configuration_request.CreateTeamsChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.create_teams_channel_configuration_result.CreateTeamsChannelConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.create_microsoft_teams_channel_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.create_microsoft_teams_channel_configuration.async_create_microsoft_teams_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.create_teams_channel_configuration_request.CreateTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["channel_id"] = channel_id
        if channel_name is not None:
            input_["channel_name"] = channel_name
        input_["team_id"] = team_id
        if team_name is not None:
            input_["team_name"] = team_name
        input_["tenant_id"] = tenant_id
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        input_["iam_role_arn"] = iam_role_arn
        input_["configuration_name"] = configuration_name
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if guardrail_policy_arns is not None:
            input_["guardrail_policy_arns"] = guardrail_policy_arns
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def create_slack_channel_configuration(
        self,
        slack_team_id: "aws_sdk_chatbot.types.slack_team_id.SlackTeamId",
        slack_channel_id: "aws_sdk_chatbot.types.slack_channel_id.SlackChannelId",
        iam_role_arn: "aws_sdk_chatbot.types.arn.Arn",
        configuration_name: "aws_sdk_chatbot.types.configuration_name.ConfigurationName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        slack_channel_name: Optional[
            "aws_sdk_chatbot.types.slack_channel_display_name.SlackChannelDisplayName"
        ] = None,
        sns_topic_arns: Optional[
            "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        logging_level: Optional[
            "aws_sdk_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        guardrail_policy_arns: Optional[
            "aws_sdk_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
        ] = None,
        user_authorization_required: Optional[
            "aws_sdk_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
        tags: Optional["aws_sdk_chatbot.types.tags.Tags"] = None,
    ) -> "aws_sdk_chatbot.types.create_slack_channel_configuration_result.CreateSlackChannelConfigurationResult":
        r"""<p>Creates an AWS Chatbot confugration for Slack.</p>

        Args:
            slack_team_id: <p>The ID of the Slack workspace authorized with AWS Chatbot.</p>
            slack_channel_id: <p>The ID of the Slack channel.</p> <p>To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ. </p>
            slack_channel_name: <p>The name of the Slack channel.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            configuration_name: <p>The name of the configuration.</p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            guardrail_policy_arns: <p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>
            tags: <p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.create_slack_channel_configuration_request.CreateSlackChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.create_slack_channel_configuration_result.CreateSlackChannelConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.create_slack_channel_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.create_slack_channel_configuration.async_create_slack_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.create_slack_channel_configuration_request.CreateSlackChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["slack_team_id"] = slack_team_id
        input_["slack_channel_id"] = slack_channel_id
        if slack_channel_name is not None:
            input_["slack_channel_name"] = slack_channel_name
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        input_["iam_role_arn"] = iam_role_arn
        input_["configuration_name"] = configuration_name
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if guardrail_policy_arns is not None:
            input_["guardrail_policy_arns"] = guardrail_policy_arns
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_chime_webhook_configuration(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.delete_chime_webhook_configuration_result.DeleteChimeWebhookConfigurationResult":
        """<p>Deletes a Amazon Chime webhook configuration for AWS Chatbot.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.delete_chime_webhook_configuration_request.DeleteChimeWebhookConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.delete_chime_webhook_configuration_result.DeleteChimeWebhookConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_chime_webhook_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_chime_webhook_configuration.async_delete_chime_webhook_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.delete_chime_webhook_configuration_request.DeleteChimeWebhookConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_microsoft_teams_channel_configuration(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.delete_teams_channel_configuration_result.DeleteTeamsChannelConfigurationResult":
        """<p>Deletes a Microsoft Teams channel configuration for AWS Chatbot</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.delete_teams_channel_configuration_request.DeleteTeamsChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.delete_teams_channel_configuration_result.DeleteTeamsChannelConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_channel_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_channel_configuration.async_delete_microsoft_teams_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.delete_teams_channel_configuration_request.DeleteTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_microsoft_teams_configured_team(
        self,
        team_id: "aws_sdk_chatbot.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.delete_teams_configured_team_result.DeleteTeamsConfiguredTeamResult":
        r"""<p>Deletes the Microsoft Teams team authorization allowing for channels to be configured in that Microsoft Teams team. Note that the Microsoft Teams team must have no channels configured to remove it. </p>

        Args:
            team_id: <p>The ID of the Microsoft Teams team authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup\">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.delete_teams_configured_team_request.DeleteTeamsConfiguredTeamRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.delete_teams_configured_team_result.DeleteTeamsConfiguredTeamResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_configured_team

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_configured_team.async_delete_microsoft_teams_configured_team(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.delete_teams_configured_team_request.DeleteTeamsConfiguredTeamRequest = {}  # type: ignore[typeddict-item]
        input_["team_id"] = team_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_microsoft_teams_user_identity(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        user_id: "aws_sdk_chatbot.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.delete_microsoft_teams_user_identity_result.DeleteMicrosoftTeamsUserIdentityResult":
        """<p>Identifes a user level permission for a channel configuration.</p>

        Args:
            chat_configuration_arn: <p>The ARN of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>
            user_id: <p>The Microsoft Teams user ID.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.delete_microsoft_teams_user_identity_request.DeleteMicrosoftTeamsUserIdentityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.delete_microsoft_teams_user_identity_result.DeleteMicrosoftTeamsUserIdentityResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_user_identity

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_microsoft_teams_user_identity.async_delete_microsoft_teams_user_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.delete_microsoft_teams_user_identity_request.DeleteMicrosoftTeamsUserIdentityRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn
        input_["user_id"] = user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_slack_channel_configuration(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.delete_slack_channel_configuration_result.DeleteSlackChannelConfigurationResult":
        """<p>Deletes a Slack channel configuration for AWS Chatbot</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration to delete.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.delete_slack_channel_configuration_request.DeleteSlackChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.delete_slack_channel_configuration_result.DeleteSlackChannelConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_slack_channel_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_slack_channel_configuration.async_delete_slack_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.delete_slack_channel_configuration_request.DeleteSlackChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_slack_user_identity(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        slack_team_id: "aws_sdk_chatbot.types.slack_team_id.SlackTeamId",
        slack_user_id: "aws_sdk_chatbot.types.slack_user_id.SlackUserId",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.delete_slack_user_identity_result.DeleteSlackUserIdentityResult":
        """<p>Deletes a user level permission for a Slack channel configuration.</p>

        Args:
            chat_configuration_arn: <p>The ARN of the SlackChannelConfiguration associated with the user identity to delete.</p>
            slack_team_id: <p>The ID of the Slack workspace authorized with AWS Chatbot.</p>
            slack_user_id: <p>The ID of the user in Slack</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.delete_slack_user_identity_request.DeleteSlackUserIdentityRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.delete_slack_user_identity_result.DeleteSlackUserIdentityResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_slack_user_identity

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_slack_user_identity.async_delete_slack_user_identity(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.delete_slack_user_identity_request.DeleteSlackUserIdentityRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn
        input_["slack_team_id"] = slack_team_id
        input_["slack_user_id"] = slack_user_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete_slack_workspace_authorization(
        self,
        slack_team_id: "aws_sdk_chatbot.types.slack_team_id.SlackTeamId",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.delete_slack_workspace_authorization_result.DeleteSlackWorkspaceAuthorizationResult":
        """<p>Deletes the Slack workspace authorization that allows channels to be configured in that workspace. This requires all configured channels in the workspace to be deleted. </p>

        Args:
            slack_team_id: <p>The ID of the Slack workspace authorized with AWS Chatbot.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.delete_slack_workspace_authorization_request.DeleteSlackWorkspaceAuthorizationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.delete_slack_workspace_authorization_result.DeleteSlackWorkspaceAuthorizationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_slack_workspace_authorization

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.delete_slack_workspace_authorization.async_delete_slack_workspace_authorization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.delete_slack_workspace_authorization_request.DeleteSlackWorkspaceAuthorizationRequest = {}  # type: ignore[typeddict-item]
        input_["slack_team_id"] = slack_team_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def describe_chime_webhook_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        chat_configuration_arn: Optional[
            "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
    ) -> "aws_sdk_chatbot.types.describe_chime_webhook_configurations_result.DescribeChimeWebhookConfigurationsResult":
        """<p>Lists Amazon Chime webhook configurations optionally filtered by ChatConfigurationArn</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
            chat_configuration_arn: <p>An optional Amazon Resource Name (ARN) of a ChimeWebhookConfiguration to describe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.describe_chime_webhook_configurations_request.DescribeChimeWebhookConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.describe_chime_webhook_configurations_result.DescribeChimeWebhookConfigurationsResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.describe_chime_webhook_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.describe_chime_webhook_configurations.async_describe_chime_webhook_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.describe_chime_webhook_configurations_request.DescribeChimeWebhookConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if chat_configuration_arn is not None:
            input_["chat_configuration_arn"] = chat_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_chime_webhook_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        chat_configuration_arn: Optional[
            "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_chatbot.types.chime_webhook_configuration.ChimeWebhookConfiguration]":
        _token = next_token
        while True:
            _response = await self.describe_chime_webhook_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                chat_configuration_arn=chat_configuration_arn,
            )
            _page = _resolve_path(_response, ("webhook_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_slack_channel_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        chat_configuration_arn: Optional[
            "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
    ) -> "aws_sdk_chatbot.types.describe_slack_channel_configurations_result.DescribeSlackChannelConfigurationsResult":
        """<p>Lists Slack channel configurations optionally filtered by ChatConfigurationArn</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>
            next_token: <p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
            chat_configuration_arn: <p>An optional Amazon Resource Name (ARN) of a SlackChannelConfiguration to describe.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.describe_slack_channel_configurations_request.DescribeSlackChannelConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.describe_slack_channel_configurations_result.DescribeSlackChannelConfigurationsResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.describe_slack_channel_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.describe_slack_channel_configurations.async_describe_slack_channel_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.describe_slack_channel_configurations_request.DescribeSlackChannelConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if chat_configuration_arn is not None:
            input_["chat_configuration_arn"] = chat_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_slack_channel_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        chat_configuration_arn: Optional[
            "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_chatbot.types.slack_channel_configuration.SlackChannelConfiguration]":
        _token = next_token
        while True:
            _response = await self.describe_slack_channel_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                chat_configuration_arn=chat_configuration_arn,
            )
            _page = _resolve_path(_response, ("slack_channel_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_slack_user_identities(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        chat_configuration_arn: Optional[
            "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_chatbot.types.describe_slack_user_identities_result.DescribeSlackUserIdentitiesResult":
        """<p>Lists all Slack user identities with a mapped role.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration associated with the user identities to describe.</p>
            next_token: <p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.describe_slack_user_identities_request.DescribeSlackUserIdentitiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.describe_slack_user_identities_result.DescribeSlackUserIdentitiesResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.describe_slack_user_identities

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.describe_slack_user_identities.async_describe_slack_user_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.describe_slack_user_identities_request.DescribeSlackUserIdentitiesRequest = {}  # type: ignore[typeddict-item]
        if chat_configuration_arn is not None:
            input_["chat_configuration_arn"] = chat_configuration_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_describe_slack_user_identities(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        chat_configuration_arn: Optional[
            "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_chatbot.types.slack_user_identity.SlackUserIdentity]":
        _token = next_token
        while True:
            _response = await self.describe_slack_user_identities(
                config_overrides=config_overrides,
                chat_configuration_arn=chat_configuration_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("slack_user_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_slack_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_chatbot.types.describe_slack_workspaces_result.DescribeSlackWorkspacesResult":
        """<p>List all authorized Slack workspaces connected to the AWS Account onboarded with AWS Chatbot.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>
            next_token: <p> An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.describe_slack_workspaces_request.DescribeSlackWorkspacesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.describe_slack_workspaces_result.DescribeSlackWorkspacesResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.describe_slack_workspaces

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.describe_slack_workspaces.async_describe_slack_workspaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.describe_slack_workspaces_request.DescribeSlackWorkspacesRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_describe_slack_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_chatbot.types.slack_workspace.SlackWorkspace]":
        _token = next_token
        while True:
            _response = await self.describe_slack_workspaces(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("slack_workspaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disassociate_from_configuration(
        self,
        resource: "aws_sdk_chatbot.types.resource_identifier.ResourceIdentifier",
        chat_configuration: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.disassociate_from_configuration_result.DisassociateFromConfigurationResult":
        """<p>Unlink a resource, for example a custom action, from a channel configuration.</p>

        Args:
            resource: <p>The resource (for example, a custom action) Amazon Resource Name (ARN) to unlink.</p>
            chat_configuration: <p>The channel configuration the resource is being disassociated from.</p>

        Examples:
            Disassociate a custom action from a configuration

            >>> await client.disassociate_from_configuration(resource='arn:aws:chatbot::1234567890:custom-action/my-custom-action', chat_configuration='arn:aws:chatbot::1234567890:chat-configuration/slack-channel/my-channel')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.disassociate_from_configuration_request.DisassociateFromConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.disassociate_from_configuration_result.DisassociateFromConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.disassociate_from_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.disassociate_from_configuration.async_disassociate_from_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.disassociate_from_configuration_request.DisassociateFromConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["resource"] = resource
        input_["chat_configuration"] = chat_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_account_preferences(
        self, *, config_overrides: Optional[AsyncchatbotClientConfig] = None
    ) -> "aws_sdk_chatbot.types.get_account_preferences_result.GetAccountPreferencesResult":
        """<p>Returns AWS Chatbot account preferences.</p>"""

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.get_account_preferences_request.GetAccountPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.get_account_preferences_result.GetAccountPreferencesResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.get_account_preferences

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.get_account_preferences.async_get_account_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.get_account_preferences_request.GetAccountPreferencesRequest = {}  # type: ignore[typeddict-item]

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def get_microsoft_teams_channel_configuration(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.get_teams_channel_configuration_result.GetTeamsChannelConfigurationResult":
        """<p>Returns a Microsoft Teams channel configuration in an AWS account.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration to retrieve.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.get_teams_channel_configuration_request.GetTeamsChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.get_teams_channel_configuration_result.GetTeamsChannelConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.get_microsoft_teams_channel_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.get_microsoft_teams_channel_configuration.async_get_microsoft_teams_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.get_teams_channel_configuration_request.GetTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list_associations(
        self,
        chat_configuration: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_chatbot.types.string.String"] = None,
    ) -> "aws_sdk_chatbot.types.list_associations_result.ListAssociationsResult":
        """<p>Lists resources associated with a channel configuration.</p>

        Args:
            chat_configuration: <p>The channel configuration to list associations for.</p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>

        Examples:
            List custom actions associated with a configuration

            >>> await client.list_associations(chat_configuration='arn:aws:chatbot::1234567890:chat-configuration/slack-channel/my-channel')
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.list_associations_request.ListAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.list_associations_result.ListAssociationsResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_associations

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_associations.async_list_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.list_associations_request.ListAssociationsRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration"] = chat_configuration
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

    async def iter_list_associations(
        self,
        chat_configuration: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["aws_sdk_chatbot.types.string.String"] = None,
    ) -> "AsyncIterator[aws_sdk_chatbot.types.association_listing.AssociationListing]":
        _token = next_token
        while True:
            _response = await self.list_associations(
                chat_configuration,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_microsoft_teams_channel_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        team_id: Optional["aws_sdk_chatbot.types.uuid.UUID"] = None,
    ) -> "aws_sdk_chatbot.types.list_teams_channel_configurations_result.ListTeamsChannelConfigurationsResult":
        r"""<p>Lists all AWS Chatbot Microsoft Teams channel configurations in an AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>
            team_id: <p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup\">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.list_teams_channel_configurations_request.ListTeamsChannelConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.list_teams_channel_configurations_result.ListTeamsChannelConfigurationsResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_channel_configurations

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_channel_configurations.async_list_microsoft_teams_channel_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.list_teams_channel_configurations_request.ListTeamsChannelConfigurationsRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if team_id is not None:
            input_["team_id"] = team_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_microsoft_teams_channel_configurations(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        team_id: Optional["aws_sdk_chatbot.types.uuid.UUID"] = None,
    ) -> "AsyncIterator[aws_sdk_chatbot.types.teams_channel_configuration.TeamsChannelConfiguration]":
        _token = next_token
        while True:
            _response = await self.list_microsoft_teams_channel_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                team_id=team_id,
            )
            _page = _resolve_path(_response, ("team_channel_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_microsoft_teams_configured_teams(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "aws_sdk_chatbot.types.list_microsoft_teams_configured_teams_result.ListMicrosoftTeamsConfiguredTeamsResult":
        """<p>Lists all authorized Microsoft Teams for an AWS Account</p>

        Args:
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.list_microsoft_teams_configured_teams_request.ListMicrosoftTeamsConfiguredTeamsRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.list_microsoft_teams_configured_teams_result.ListMicrosoftTeamsConfiguredTeamsResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_configured_teams

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_configured_teams.async_list_microsoft_teams_configured_teams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.list_microsoft_teams_configured_teams_request.ListMicrosoftTeamsConfiguredTeamsRequest = {}  # type: ignore[typeddict-item]
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

    async def iter_list_microsoft_teams_configured_teams(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[aws_sdk_chatbot.types.configured_team.ConfiguredTeam]":
        _token = next_token
        while True:
            _response = await self.list_microsoft_teams_configured_teams(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("configured_teams",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_microsoft_teams_user_identities(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        chat_configuration_arn: Optional[
            "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
    ) -> "aws_sdk_chatbot.types.list_microsoft_teams_user_identities_result.ListMicrosoftTeamsUserIdentitiesResult":
        """<p>A list all Microsoft Teams user identities with a mapped role.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identities to list.</p>
            next_token: <p>An optional token returned from a prior request. Use this token for pagination of results from this action. If this parameter is specified, the response includes only results beyond the token, up to the value specified by MaxResults. </p>
            max_results: <p>The maximum number of results to include in the response. If more results exist than the specified MaxResults value, a token is included in the response so that the remaining results can be retrieved. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.list_microsoft_teams_user_identities_request.ListMicrosoftTeamsUserIdentitiesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.list_microsoft_teams_user_identities_result.ListMicrosoftTeamsUserIdentitiesResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_user_identities

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_microsoft_teams_user_identities.async_list_microsoft_teams_user_identities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.list_microsoft_teams_user_identities_request.ListMicrosoftTeamsUserIdentitiesRequest = {}  # type: ignore[typeddict-item]
        if chat_configuration_arn is not None:
            input_["chat_configuration_arn"] = chat_configuration_arn
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def iter_list_microsoft_teams_user_identities(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        chat_configuration_arn: Optional[
            "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
        ] = None,
        next_token: Optional[
            "aws_sdk_chatbot.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["aws_sdk_chatbot.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[aws_sdk_chatbot.types.teams_user_identity.TeamsUserIdentity]":
        _token = next_token
        while True:
            _response = await self.list_microsoft_teams_user_identities(
                config_overrides=config_overrides,
                chat_configuration_arn=chat_configuration_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("teams_user_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "aws_sdk_chatbot.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a user, server, or role.</p>

        Args:
            resource_arn: <p>The ARN of the resource to list tags for.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_tags_for_resource

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def tag_resource(
        self,
        resource_arn: "aws_sdk_chatbot.types.amazon_resource_name.AmazonResourceName",
        tags: "aws_sdk_chatbot.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.tag_resource_response.TagResourceResponse":
        """<p>Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.</p>

        Args:
            resource_arn: <p>The ARN of the configuration.</p>
            tags: <p>A list of tags to apply to the configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.tag_resource_response.TagResourceResponse"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.tag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.tag_resource_request.TagResourceRequest = {}  # type: ignore[typeddict-item]
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
        resource_arn: "aws_sdk_chatbot.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "aws_sdk_chatbot.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
    ) -> "aws_sdk_chatbot.types.untag_resource_response.UntagResourceResponse":
        """<p>Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.</p>

        Args:
            resource_arn: <p>The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.</p>
            tag_keys: <p>TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.untag_resource_response.UntagResourceResponse"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.untag_resource

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.untag_resource_request.UntagResourceRequest = {}  # type: ignore[typeddict-item]
        input_["resource_arn"] = resource_arn
        input_["tag_keys"] = tag_keys

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_account_preferences(
        self,
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        user_authorization_required: Optional[
            "aws_sdk_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
        training_data_collection_enabled: Optional[
            "aws_sdk_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
    ) -> "aws_sdk_chatbot.types.update_account_preferences_result.UpdateAccountPreferencesResult":
        """<p>Updates AWS Chatbot account preferences.</p>

        Args:
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>
            training_data_collection_enabled: <p>Turns on training data collection.</p> <p>This helps improve the AWS Chatbot experience by allowing AWS Chatbot to store and use your customer information, such as AWS Chatbot configurations, notifications, user inputs, AWS Chatbot generated responses, and interaction data. This data helps us to continuously improve and develop Artificial Intelligence (AI) technologies. Your data is not shared with any third parties and is protected using sophisticated controls to prevent unauthorized access and misuse. AWS Chatbot does not store or use interactions in chat channels with Amazon Q for training AI technologies for AWS Chatbot. </p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.update_account_preferences_request.UpdateAccountPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.update_account_preferences_result.UpdateAccountPreferencesResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.update_account_preferences

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.update_account_preferences.async_update_account_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.update_account_preferences_request.UpdateAccountPreferencesRequest = {}  # type: ignore[typeddict-item]
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required
        if training_data_collection_enabled is not None:
            input_["training_data_collection_enabled"] = (
                training_data_collection_enabled
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_chime_webhook_configuration(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        webhook_description: Optional[
            "aws_sdk_chatbot.types.chime_webhook_description.ChimeWebhookDescription"
        ] = None,
        webhook_url: Optional[
            "aws_sdk_chatbot.types.chime_webhook_url.ChimeWebhookUrl"
        ] = None,
        sns_topic_arns: Optional[
            "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        iam_role_arn: Optional["aws_sdk_chatbot.types.arn.Arn"] = None,
        logging_level: Optional[
            "aws_sdk_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
    ) -> "aws_sdk_chatbot.types.update_chime_webhook_configuration_result.UpdateChimeWebhookConfigurationResult":
        r"""<p>Updates a Amazon Chime webhook configuration.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration to update.</p>
            webhook_description: <p>A description of the webhook. We recommend using the convention <code>RoomName/WebhookName</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html\">Tutorial: Get started with Amazon Chime</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            webhook_url: <p>The URL for the Amazon Chime webhook.</p>
            sns_topic_arns: <p>The ARNs of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.update_chime_webhook_configuration_request.UpdateChimeWebhookConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.update_chime_webhook_configuration_result.UpdateChimeWebhookConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.update_chime_webhook_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.update_chime_webhook_configuration.async_update_chime_webhook_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.update_chime_webhook_configuration_request.UpdateChimeWebhookConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn
        if webhook_description is not None:
            input_["webhook_description"] = webhook_description
        if webhook_url is not None:
            input_["webhook_url"] = webhook_url
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if logging_level is not None:
            input_["logging_level"] = logging_level

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_microsoft_teams_channel_configuration(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        channel_id: "aws_sdk_chatbot.types.teams_channel_id.TeamsChannelId",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        channel_name: Optional[
            "aws_sdk_chatbot.types.teams_channel_name.TeamsChannelName"
        ] = None,
        sns_topic_arns: Optional[
            "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        iam_role_arn: Optional["aws_sdk_chatbot.types.arn.Arn"] = None,
        logging_level: Optional[
            "aws_sdk_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        guardrail_policy_arns: Optional[
            "aws_sdk_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
        ] = None,
        user_authorization_required: Optional[
            "aws_sdk_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
    ) -> "aws_sdk_chatbot.types.update_teams_channel_configuration_result.UpdateTeamsChannelConfigurationResult":
        r"""<p>Updates an Microsoft Teams channel configuration.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the TeamsChannelConfiguration to update.</p>
            channel_id: <p>The ID of the Microsoft Teams channel.</p>
            channel_name: <p>The name of the Microsoft Teams channel.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            guardrail_policy_arns: <p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.update_teams_channel_configuration_request.UpdateTeamsChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.update_teams_channel_configuration_result.UpdateTeamsChannelConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.update_microsoft_teams_channel_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.update_microsoft_teams_channel_configuration.async_update_microsoft_teams_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.update_teams_channel_configuration_request.UpdateTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn
        input_["channel_id"] = channel_id
        if channel_name is not None:
            input_["channel_name"] = channel_name
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if guardrail_policy_arns is not None:
            input_["guardrail_policy_arns"] = guardrail_policy_arns
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update_slack_channel_configuration(
        self,
        chat_configuration_arn: "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn",
        slack_channel_id: "aws_sdk_chatbot.types.slack_channel_id.SlackChannelId",
        *,
        config_overrides: Optional[AsyncchatbotClientConfig] = None,
        slack_channel_name: Optional[
            "aws_sdk_chatbot.types.slack_channel_display_name.SlackChannelDisplayName"
        ] = None,
        sns_topic_arns: Optional[
            "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
        ] = None,
        iam_role_arn: Optional["aws_sdk_chatbot.types.arn.Arn"] = None,
        logging_level: Optional[
            "aws_sdk_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
        ] = None,
        guardrail_policy_arns: Optional[
            "aws_sdk_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
        ] = None,
        user_authorization_required: Optional[
            "aws_sdk_chatbot.types.boolean_account_preference.BooleanAccountPreference"
        ] = None,
    ) -> "aws_sdk_chatbot.types.update_slack_channel_configuration_result.UpdateSlackChannelConfigurationResult":
        r"""<p>Updates a Slack channel configuration.</p>

        Args:
            chat_configuration_arn: <p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration to update.</p>
            slack_channel_id: <p>The ID of the Slack channel.</p> <p>To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ. </p>
            slack_channel_name: <p>The name of the Slack channel.</p>
            sns_topic_arns: <p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>
            iam_role_arn: <p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>
            logging_level: <p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>
            guardrail_policy_arns: <p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>
            user_authorization_required: <p>Enables use of a user role requirement in your chat configuration.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_chatbot.types.update_slack_channel_configuration_request.UpdateSlackChannelConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_chatbot.types.update_slack_channel_configuration_result.UpdateSlackChannelConfigurationResult"
        ]:
            import aws_sdk_chatbot._operations.wheatley_orchestration_20171011.update_slack_channel_configuration

            (
                output,
                http_response,
            ) = await aws_sdk_chatbot._operations.wheatley_orchestration_20171011.update_slack_channel_configuration.async_update_slack_channel_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: aws_sdk_chatbot.types.update_slack_channel_configuration_request.UpdateSlackChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
        input_["chat_configuration_arn"] = chat_configuration_arn
        input_["slack_channel_id"] = slack_channel_id
        if slack_channel_name is not None:
            input_["slack_channel_name"] = slack_channel_name
        if sns_topic_arns is not None:
            input_["sns_topic_arns"] = sns_topic_arns
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if logging_level is not None:
            input_["logging_level"] = logging_level
        if guardrail_policy_arns is not None:
            input_["guardrail_policy_arns"] = guardrail_policy_arns
        if user_authorization_required is not None:
            input_["user_authorization_required"] = user_authorization_required

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
