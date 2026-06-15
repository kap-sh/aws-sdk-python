"""Generated from Smithy shape ``com.amazonaws.chatbot#TeamsUserIdentity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.arn
    import aws_sdk_chatbot.types.aws_user_identity
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.teams_channel_id
    import aws_sdk_chatbot.types.uuid


class TeamsUserIdentity(TypedDict):
    iam_role_arn: "aws_sdk_chatbot.types.arn.Arn"
    r"""<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    chat_configuration_arn: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the MicrosoftTeamsChannelConfiguration associated with the user identity to delete.</p>"""
    team_id: "aws_sdk_chatbot.types.uuid.UUID"
    r"""<p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup\">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    user_id: NotRequired["aws_sdk_chatbot.types.uuid.UUID"]
    """<p>The Microsoft Teams user ID.</p>"""
    aws_user_identity: NotRequired[
        "aws_sdk_chatbot.types.aws_user_identity.AwsUserIdentity"
    ]
    """<p>The AWS user identity ARN used to associate a Microsoft Teams user Identity with an IAM Role.</p>"""
    teams_channel_id: NotRequired[
        "aws_sdk_chatbot.types.teams_channel_id.TeamsChannelId"
    ]
    """<p>The ID of the Microsoft Teams channel.</p>"""
    teams_tenant_id: NotRequired["aws_sdk_chatbot.types.uuid.UUID"]
    """<p>The ID of the Microsoft Teams tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TeamsUserIdentity) -> dict:
    out: dict = {}
    out["IamRoleArn"] = value["iam_role_arn"]
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    out["TeamId"] = value["team_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "aws_user_identity" in value:
        out["AwsUserIdentity"] = value["aws_user_identity"]
    if "teams_channel_id" in value:
        out["TeamsChannelId"] = value["teams_channel_id"]
    if "teams_tenant_id" in value:
        out["TeamsTenantId"] = value["teams_tenant_id"]
    return out


def deserialize_json(data: dict) -> TeamsUserIdentity:
    out: TeamsUserIdentity = {}  # type: ignore[typeddict-item]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("TeamsUserIdentity.iam_role_arn required")
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError("TeamsUserIdentity.chat_configuration_arn required")
    if "TeamId" in data:
        out["team_id"] = data["TeamId"]
    else:
        raise DeserializationError("TeamsUserIdentity.team_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "AwsUserIdentity" in data:
        out["aws_user_identity"] = data["AwsUserIdentity"]
    if "TeamsChannelId" in data:
        out["teams_channel_id"] = data["TeamsChannelId"]
    if "TeamsTenantId" in data:
        out["teams_tenant_id"] = data["TeamsTenantId"]
    return out
