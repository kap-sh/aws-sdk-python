"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateTeamsChannelConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.arn
    import aws_sdk_chatbot.types.boolean_account_preference
    import aws_sdk_chatbot.types.configuration_name
    import aws_sdk_chatbot.types.customer_cw_log_level
    import aws_sdk_chatbot.types.guardrail_policy_arn_list
    import aws_sdk_chatbot.types.sns_topic_arn_list
    import aws_sdk_chatbot.types.tags
    import aws_sdk_chatbot.types.team_name
    import aws_sdk_chatbot.types.teams_channel_id
    import aws_sdk_chatbot.types.teams_channel_name
    import aws_sdk_chatbot.types.uuid


class CreateTeamsChannelConfigurationRequest(TypedDict):
    channel_id: "aws_sdk_chatbot.types.teams_channel_id.TeamsChannelId"
    """<p>The ID of the Microsoft Teams channel.</p>"""
    channel_name: NotRequired[
        "aws_sdk_chatbot.types.teams_channel_name.TeamsChannelName"
    ]
    """<p>The name of the Microsoft Teams channel.</p>"""
    team_id: "aws_sdk_chatbot.types.uuid.UUID"
    """<p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup\">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    team_name: NotRequired["aws_sdk_chatbot.types.team_name.TeamName"]
    """<p>The name of the Microsoft Teams Team.</p>"""
    tenant_id: "aws_sdk_chatbot.types.uuid.UUID"
    """<p>The ID of the Microsoft Teams tenant.</p>"""
    sns_topic_arns: NotRequired[
        "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.</p>"""
    iam_role_arn: "aws_sdk_chatbot.types.arn.Arn"
    """<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    configuration_name: "aws_sdk_chatbot.types.configuration_name.ConfigurationName"
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


# --- restJson1 ser/de ---
def serialize_json(value: CreateTeamsChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["ChannelId"] = value["channel_id"]
    if "channel_name" in value:
        out["ChannelName"] = value["channel_name"]
    out["TeamId"] = value["team_id"]
    if "team_name" in value:
        out["TeamName"] = value["team_name"]
    out["TenantId"] = value["tenant_id"]
    if "sns_topic_arns" in value:
        import aws_sdk_chatbot.types.sns_topic_arn_list

        out["SnsTopicArns"] = aws_sdk_chatbot.types.sns_topic_arn_list.serialize_json(
            value["sns_topic_arns"]
        )
    out["IamRoleArn"] = value["iam_role_arn"]
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
    return out


def deserialize_json(data: dict) -> CreateTeamsChannelConfigurationRequest:
    out: CreateTeamsChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ChannelId" in data:
        out["channel_id"] = data["ChannelId"]
    else:
        raise DeserializationError(
            "CreateTeamsChannelConfigurationRequest.channel_id required"
        )
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    if "TeamId" in data:
        out["team_id"] = data["TeamId"]
    else:
        raise DeserializationError(
            "CreateTeamsChannelConfigurationRequest.team_id required"
        )
    if "TeamName" in data:
        out["team_name"] = data["TeamName"]
    if "TenantId" in data:
        out["tenant_id"] = data["TenantId"]
    else:
        raise DeserializationError(
            "CreateTeamsChannelConfigurationRequest.tenant_id required"
        )
    if "SnsTopicArns" in data:
        import aws_sdk_chatbot.types.sns_topic_arn_list

        out["sns_topic_arns"] = (
            aws_sdk_chatbot.types.sns_topic_arn_list.deserialize_json(
                data["SnsTopicArns"]
            )
        )
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError(
            "CreateTeamsChannelConfigurationRequest.iam_role_arn required"
        )
    if "ConfigurationName" in data:
        out["configuration_name"] = data["ConfigurationName"]
    else:
        raise DeserializationError(
            "CreateTeamsChannelConfigurationRequest.configuration_name required"
        )
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
    return out
