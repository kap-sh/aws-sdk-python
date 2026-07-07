"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendVoiceMessageResult``."""

from typing_extensions import NotRequired, TypedDict


class SendVoiceMessageResult(TypedDict, closed=True):
    message_id: NotRequired["str"]
    """<p>The unique identifier for the message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendVoiceMessageResult) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendVoiceMessageResult:
    out: SendVoiceMessageResult = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    return out
