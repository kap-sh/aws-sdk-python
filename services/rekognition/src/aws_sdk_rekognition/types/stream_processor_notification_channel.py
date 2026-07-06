"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorNotificationChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.sns_topic_arn


class StreamProcessorNotificationChannel(TypedDict, closed=True):
    sns_topic_arn: "aws_sdk_rekognition.types.sns_topic_arn.SNSTopicArn"
    """<p> The Amazon Resource Number (ARN) of the Amazon Amazon Simple Notification Service topic to which Amazon Rekognition posts the completion status. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorNotificationChannel) -> dict:
    out: dict = {}
    out["SNSTopicArn"] = value["sns_topic_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessorNotificationChannel:
    out: StreamProcessorNotificationChannel = {}  # type: ignore[typeddict-item]
    if "SNSTopicArn" in data:
        out["sns_topic_arn"] = data["SNSTopicArn"]
    else:
        raise DeserializationError(
            "StreamProcessorNotificationChannel.sns_topic_arn required"
        )
    return out
