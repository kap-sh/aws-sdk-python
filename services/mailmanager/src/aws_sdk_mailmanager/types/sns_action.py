"""Generated from Smithy shape ``com.amazonaws.mailmanager#SnsAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.action_failure_policy
    import aws_sdk_mailmanager.types.iam_role_arn
    import aws_sdk_mailmanager.types.sns_notification_encoding
    import aws_sdk_mailmanager.types.sns_notification_payload_type
    import aws_sdk_mailmanager.types.sns_topic_arn


class SnsAction(TypedDict):
    action_failure_policy: NotRequired[
        "aws_sdk_mailmanager.types.action_failure_policy.ActionFailurePolicy"
    ]
    """<p>A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, specified SNS topic has been deleted or the role lacks necessary permissions to call the <code>sns:Publish</code> API.</p>"""
    topic_arn: "aws_sdk_mailmanager.types.sns_topic_arn.SnsTopicArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS Topic to which notification for the email received will be published.</p>"""
    role_arn: "aws_sdk_mailmanager.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Role to use while writing to Amazon SNS. This role must have access to the <code>sns:Publish</code> API for the given topic.</p>"""
    encoding: (
        "aws_sdk_mailmanager.types.sns_notification_encoding.SnsNotificationEncoding"
    )
    """<p>The encoding to use for the email within the Amazon SNS notification. The default value is <code>UTF-8</code>. Use <code>BASE64</code> if you need to preserve all special characters, especially when the original message uses a different encoding format.</p>"""
    payload_type: "aws_sdk_mailmanager.types.sns_notification_payload_type.SnsNotificationPayloadType"
    """<p>The expected payload type within the Amazon SNS notification. <code>CONTENT</code> attempts to publish the full email content with 20KB of headers content. <code>HEADERS</code> extracts up to 100KB of header content to include in the notification, email content will not be included to the notification. The default value is <code>CONTENT</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SnsAction) -> dict:
    out: dict = {}
    if "action_failure_policy" in value:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["ActionFailurePolicy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.serialize_aws_json_1_0(
                value["action_failure_policy"]
            )
        )
    out["TopicArn"] = value["topic_arn"]
    out["RoleArn"] = value["role_arn"]
    import aws_sdk_mailmanager.types.sns_notification_encoding

    out["Encoding"] = (
        aws_sdk_mailmanager.types.sns_notification_encoding.serialize_aws_json_1_0(
            value.get("encoding", "UTF-8")
        )
    )
    import aws_sdk_mailmanager.types.sns_notification_payload_type

    out["PayloadType"] = (
        aws_sdk_mailmanager.types.sns_notification_payload_type.serialize_aws_json_1_0(
            value.get("payload_type", "CONTENT")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SnsAction:
    out: SnsAction = {}  # type: ignore[typeddict-item]
    if "ActionFailurePolicy" in data:
        import aws_sdk_mailmanager.types.action_failure_policy

        out["action_failure_policy"] = (
            aws_sdk_mailmanager.types.action_failure_policy.deserialize_aws_json_1_0(
                data["ActionFailurePolicy"]
            )
        )
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    else:
        raise DeserializationError("SnsAction.topic_arn required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("SnsAction.role_arn required")
    if "Encoding" in data:
        import aws_sdk_mailmanager.types.sns_notification_encoding

        out["encoding"] = (
            aws_sdk_mailmanager.types.sns_notification_encoding.deserialize_aws_json_1_0(
                data["Encoding"]
            )
        )
    else:
        out["encoding"] = "UTF-8"
    if "PayloadType" in data:
        import aws_sdk_mailmanager.types.sns_notification_payload_type

        out["payload_type"] = (
            aws_sdk_mailmanager.types.sns_notification_payload_type.deserialize_aws_json_1_0(
                data["PayloadType"]
            )
        )
    else:
        out["payload_type"] = "CONTENT"
    return out
