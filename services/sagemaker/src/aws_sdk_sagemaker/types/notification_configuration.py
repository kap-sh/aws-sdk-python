"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotificationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.notification_topic_arn


class NotificationConfiguration(TypedDict):
    notification_topic_arn: NotRequired[
        "aws_sdk_sagemaker.types.notification_topic_arn.NotificationTopicArn"
    ]
    """<p>The ARN for the Amazon SNS topic to which notifications should be published.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationConfiguration) -> dict:
    out: dict = {}
    if "notification_topic_arn" in value:
        out["NotificationTopicArn"] = value["notification_topic_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "NotificationTopicArn" in data:
        out["notification_topic_arn"] = data["NotificationTopicArn"]
    return out
