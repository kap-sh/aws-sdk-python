"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PutMessageFeedbackResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.message_feedback_status
    import aws_sdk_pinpoint_sms_voice_v2.types.message_id


class PutMessageFeedbackResult(TypedDict):
    message_id: "aws_sdk_pinpoint_sms_voice_v2.types.message_id.MessageId"
    """<p>The unique identifier for the message.</p>"""
    message_feedback_status: "aws_sdk_pinpoint_sms_voice_v2.types.message_feedback_status.MessageFeedbackStatus"
    """<p>The current status of the message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMessageFeedbackResult) -> dict:
    out: dict = {}
    out["MessageId"] = value["message_id"]
    out["MessageFeedbackStatus"] = value["message_feedback_status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMessageFeedbackResult:
    out: PutMessageFeedbackResult = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    else:
        raise DeserializationError("PutMessageFeedbackResult.message_id required")
    if "MessageFeedbackStatus" in data:
        out["message_feedback_status"] = data["MessageFeedbackStatus"]
    else:
        raise DeserializationError(
            "PutMessageFeedbackResult.message_feedback_status required"
        )
    return out
