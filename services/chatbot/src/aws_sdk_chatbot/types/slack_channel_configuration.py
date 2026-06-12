"""Generated from Smithy shape ``com.amazonaws.chatbot#SlackChannelConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.arn
    import aws_sdk_chatbot.types.boolean_account_preference
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.configuration_name
    import aws_sdk_chatbot.types.customer_cw_log_level
    import aws_sdk_chatbot.types.guardrail_policy_arn_list
    import aws_sdk_chatbot.types.resource_state
    import aws_sdk_chatbot.types.slack_channel_display_name
    import aws_sdk_chatbot.types.slack_channel_id
    import aws_sdk_chatbot.types.slack_team_id
    import aws_sdk_chatbot.types.slack_team_name
    import aws_sdk_chatbot.types.sns_topic_arn_list
    import aws_sdk_chatbot.types.string
    import aws_sdk_chatbot.types.tags


class SlackChannelConfiguration(TypedDict):
    slack_team_name: "aws_sdk_chatbot.types.slack_team_name.SlackTeamName"
    """<p>Name of the Slack workspace.</p>"""
    slack_team_id: "aws_sdk_chatbot.types.slack_team_id.SlackTeamId"
    """<p>The ID of the Slack workspace authorized with Amazon Chime.</p>"""
    slack_channel_id: "aws_sdk_chatbot.types.slack_channel_id.SlackChannelId"
    """<p>The ID of the Slack channel.</p> <p>To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ. </p>"""
    slack_channel_name: (
        "aws_sdk_chatbot.types.slack_channel_display_name.SlackChannelDisplayName"
    )
    """<p>The name of the Slack channel.</p>"""
    chat_configuration_arn: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the SlackChannelConfiguration.</p>"""
    iam_role_arn: "aws_sdk_chatbot.types.arn.Arn"
    """<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    sns_topic_arns: "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
    """<p>The ARNs of the SNS topics that deliver notifications to AWS Chatbot.</p>"""
    configuration_name: NotRequired[
        "aws_sdk_chatbot.types.configuration_name.ConfigurationName"
    ]
    """<p>The name of the configuration.</p>"""
    logging_level: NotRequired[
        "aws_sdk_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
    ]
    """<p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>"""
    guardrail_policy_arns: NotRequired[
        "aws_sdk_chatbot.types.guardrail_policy_arn_list.GuardrailPolicyArnList"
    ]
    """<p>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed <code>AdministratorAccess</code> policy is applied by default if this is not set. </p>"""
    user_authorization_required: NotRequired[
        "aws_sdk_chatbot.types.boolean_account_preference.BooleanAccountPreference"
    ]
    """<p>Enables use of a user role requirement in your chat configuration.</p>"""
    tags: NotRequired["aws_sdk_chatbot.types.tags.Tags"]
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""
    state: NotRequired["aws_sdk_chatbot.types.resource_state.ResourceState"]
    """<p>Either <code>ENABLED</code> or <code>DISABLED</code>. The resource returns <code>DISABLED</code> if the organization's AWS Chatbot policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.</p>"""
    state_reason: NotRequired["aws_sdk_chatbot.types.string.String"]
    """<p>Provided if State is <code>DISABLED</code>. Provides context as to why the resource is disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackChannelConfiguration) -> dict:
    out: dict = {}
    out["SlackTeamName"] = value["slack_team_name"]
    out["SlackTeamId"] = value["slack_team_id"]
    out["SlackChannelId"] = value["slack_channel_id"]
    out["SlackChannelName"] = value["slack_channel_name"]
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    out["IamRoleArn"] = value["iam_role_arn"]
    import aws_sdk_chatbot.types.sns_topic_arn_list

    out["SnsTopicArns"] = aws_sdk_chatbot.types.sns_topic_arn_list.serialize_json(
        value["sns_topic_arns"]
    )
    if "configuration_name" in value:
        out["ConfigurationName"] = value["configuration_name"]
    if "logging_level" in value:
        out["LoggingLevel"] = value["logging_level"]
    if "guardrail_policy_arns" in value:
        import aws_sdk_chatbot.types.guardrail_policy_arn_list

        out["GuardrailPolicyArns"] = (
            aws_sdk_chatbot.types.guardrail_policy_arn_list.serialize_json(
                value["guardrail_policy_arns"]
            )
        )
    if "user_authorization_required" in value:
        out["UserAuthorizationRequired"] = value["user_authorization_required"]
    if "tags" in value:
        import aws_sdk_chatbot.types.tags

        out["Tags"] = aws_sdk_chatbot.types.tags.serialize_json(value["tags"])
    if "state" in value:
        out["State"] = value["state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    return out


def deserialize_json(data: dict) -> SlackChannelConfiguration:
    out: SlackChannelConfiguration = {}  # type: ignore[typeddict-item]
    if "SlackTeamName" in data:
        out["slack_team_name"] = data["SlackTeamName"]
    else:
        raise DeserializationError("SlackChannelConfiguration.slack_team_name required")
    if "SlackTeamId" in data:
        out["slack_team_id"] = data["SlackTeamId"]
    else:
        raise DeserializationError("SlackChannelConfiguration.slack_team_id required")
    if "SlackChannelId" in data:
        out["slack_channel_id"] = data["SlackChannelId"]
    else:
        raise DeserializationError(
            "SlackChannelConfiguration.slack_channel_id required"
        )
    if "SlackChannelName" in data:
        out["slack_channel_name"] = data["SlackChannelName"]
    else:
        raise DeserializationError(
            "SlackChannelConfiguration.slack_channel_name required"
        )
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError(
            "SlackChannelConfiguration.chat_configuration_arn required"
        )
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("SlackChannelConfiguration.iam_role_arn required")
    if "SnsTopicArns" in data:
        import aws_sdk_chatbot.types.sns_topic_arn_list

        out["sns_topic_arns"] = (
            aws_sdk_chatbot.types.sns_topic_arn_list.deserialize_json(
                data["SnsTopicArns"]
            )
        )
    else:
        raise DeserializationError("SlackChannelConfiguration.sns_topic_arns required")
    if "ConfigurationName" in data:
        out["configuration_name"] = data["ConfigurationName"]
    if "LoggingLevel" in data:
        out["logging_level"] = data["LoggingLevel"]
    if "GuardrailPolicyArns" in data:
        import aws_sdk_chatbot.types.guardrail_policy_arn_list

        out["guardrail_policy_arns"] = (
            aws_sdk_chatbot.types.guardrail_policy_arn_list.deserialize_json(
                data["GuardrailPolicyArns"]
            )
        )
    if "UserAuthorizationRequired" in data:
        out["user_authorization_required"] = data["UserAuthorizationRequired"]
    if "Tags" in data:
        import aws_sdk_chatbot.types.tags

        out["tags"] = aws_sdk_chatbot.types.tags.deserialize_json(data["Tags"])
    if "State" in data:
        out["state"] = data["State"]
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    return out
