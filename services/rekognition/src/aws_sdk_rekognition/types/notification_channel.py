"""Generated from Smithy shape ``com.amazonaws.rekognition#NotificationChannel``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.role_arn
    import aws_sdk_rekognition.types.sns_topic_arn


class NotificationChannel(TypedDict):
    sns_topic_arn: "aws_sdk_rekognition.types.sns_topic_arn.SNSTopicArn"
    """<p>The Amazon SNS topic to which Amazon Rekognition posts the completion status.</p>"""
    role_arn: "aws_sdk_rekognition.types.role_arn.RoleArn"
    """<p>The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationChannel) -> dict:
    out: dict = {}
    out["SNSTopicArn"] = value["sns_topic_arn"]
    out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationChannel:
    out: NotificationChannel = {}  # type: ignore[typeddict-item]
    if "SNSTopicArn" in data:
        out["sns_topic_arn"] = data["SNSTopicArn"]
    else:
        raise DeserializationError("NotificationChannel.sns_topic_arn required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("NotificationChannel.role_arn required")
    return out
