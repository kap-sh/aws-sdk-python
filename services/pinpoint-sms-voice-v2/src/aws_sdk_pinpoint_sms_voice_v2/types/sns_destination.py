"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SnsDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.sns_topic_arn


class SnsDestination(TypedDict, closed=True):
    topic_arn: "aws_sdk_pinpoint_sms_voice_v2.types.sns_topic_arn.SnsTopicArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SnsDestination) -> dict:
    out: dict = {}
    out["TopicArn"] = value["topic_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SnsDestination:
    out: SnsDestination = {}  # type: ignore[typeddict-item]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    else:
        raise DeserializationError("SnsDestination.topic_arn required")
    return out
