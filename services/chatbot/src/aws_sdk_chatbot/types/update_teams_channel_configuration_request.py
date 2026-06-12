"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateTeamsChannelConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.arn
    import aws_sdk_chatbot.types.boolean_account_preference
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.customer_cw_log_level
    import aws_sdk_chatbot.types.guardrail_policy_arn_list
    import aws_sdk_chatbot.types.sns_topic_arn_list
    import aws_sdk_chatbot.types.teams_channel_id
    import aws_sdk_chatbot.types.teams_channel_name


class UpdateTeamsChannelConfigurationRequest(TypedDict):
    chat_configuration_arn: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the TeamsChannelConfiguration to update.</p>"""
    channel_id: "aws_sdk_chatbot.types.teams_channel_id.TeamsChannelId"
    """<p>The ID of the Microsoft Teams channel.</p>"""
    channel_name: NotRequired[
        "aws_sdk_chatbot.types.teams_channel_name.TeamsChannelName"
    ]
    """<p>The name of the Microsoft Teams channel.</p>"""
    sns_topic_arns: NotRequired[
        "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>"""
    iam_role_arn: NotRequired["aws_sdk_chatbot.types.arn.Arn"]
    """<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
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


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTeamsChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    out["ChannelId"] = value["channel_id"]
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    if "sns_topic_arns" in value:
        import aws_sdk_chatbot.types.sns_topic_arn_list

        out["SnsTopicArns"] = aws_sdk_chatbot.types.sns_topic_arn_list.serialize_json(
            value["sns_topic_arns"]
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
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
    return out


def deserialize_json(data: dict) -> UpdateTeamsChannelConfigurationRequest:
    out: UpdateTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateTeamsChannelConfigurationRequest.chat_configuration_arn required"
        )
    if "ChannelId" in data:
        out["channel_id"] = data["ChannelId"]
    else:
        raise DeserializationError(
            "UpdateTeamsChannelConfigurationRequest.channel_id required"
        )
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "SnsTopicArns" in data:
        import aws_sdk_chatbot.types.sns_topic_arn_list

        out["sns_topic_arns"] = (
            aws_sdk_chatbot.types.sns_topic_arn_list.deserialize_json(
                data["SnsTopicArns"]
            )
        )
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
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
    return out
