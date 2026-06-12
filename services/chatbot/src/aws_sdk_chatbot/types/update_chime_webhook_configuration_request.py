"""Generated from Smithy shape ``com.amazonaws.chatbot#UpdateChimeWebhookConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.arn
    import aws_sdk_chatbot.types.chat_configuration_arn
    import aws_sdk_chatbot.types.chime_webhook_description
    import aws_sdk_chatbot.types.chime_webhook_url
    import aws_sdk_chatbot.types.customer_cw_log_level
    import aws_sdk_chatbot.types.sns_topic_arn_list


class UpdateChimeWebhookConfigurationRequest(TypedDict):
    chat_configuration_arn: (
        "aws_sdk_chatbot.types.chat_configuration_arn.ChatConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration to update.</p>"""
    webhook_description: NotRequired[
        "aws_sdk_chatbot.types.chime_webhook_description.ChimeWebhookDescription"
    ]
    """<p>A description of the webhook. We recommend using the convention <code>RoomName/WebhookName</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chime-setup.html\">Tutorial: Get started with Amazon Chime</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    webhook_url: NotRequired["aws_sdk_chatbot.types.chime_webhook_url.ChimeWebhookUrl"]
    """<p>The URL for the Amazon Chime webhook.</p>"""
    sns_topic_arns: NotRequired[
        "aws_sdk_chatbot.types.sns_topic_arn_list.SnsTopicArnList"
    ]
    """<p>The ARNs of the SNS topics that deliver notifications to AWS Chatbot.</p>"""
    iam_role_arn: NotRequired["aws_sdk_chatbot.types.arn.Arn"]
    """<p>A user-defined role that AWS Chatbot assumes. This is not the service-linked role.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html\">IAM policies for AWS Chatbot</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    logging_level: NotRequired[
        "aws_sdk_chatbot.types.customer_cw_log_level.CustomerCwLogLevel"
    ]
    """<p>Logging levels include <code>ERROR</code>, <code>INFO</code>, or <code>NONE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChimeWebhookConfigurationRequest) -> dict:
    out: dict = {}
    out["ChatConfigurationArn"] = value["chat_configuration_arn"]
    if "webhook_description" in value:
        out["WebhookDescription"] = value["webhook_description"]
    if "webhook_url" in value:
        out["WebhookUrl"] = value["webhook_url"]
    if "sns_topic_arns" in value:
        import aws_sdk_chatbot.types.sns_topic_arn_list

        out["SnsTopicArns"] = aws_sdk_chatbot.types.sns_topic_arn_list.serialize_json(
            value["sns_topic_arns"]
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "logging_level" in value:
        out["LoggingLevel"] = value["logging_level"]
    return out


def deserialize_json(data: dict) -> UpdateChimeWebhookConfigurationRequest:
    out: UpdateChimeWebhookConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ChatConfigurationArn" in data:
        out["chat_configuration_arn"] = data["ChatConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateChimeWebhookConfigurationRequest.chat_configuration_arn required"
        )
    if "WebhookDescription" in data:
        out["webhook_description"] = data["WebhookDescription"]
    if "WebhookUrl" in data:
        out["webhook_url"] = data["WebhookUrl"]
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
    return out
