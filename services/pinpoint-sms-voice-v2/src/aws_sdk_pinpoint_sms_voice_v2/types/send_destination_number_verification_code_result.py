"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendDestinationNumberVerificationCodeResult``."""

from typing import TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError


class SendDestinationNumberVerificationCodeResult(TypedDict):
    message_id: "str"
    """<p>The unique identifier for the message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendDestinationNumberVerificationCodeResult) -> dict:
    out: dict = {}
    out["MessageId"] = value["message_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendDestinationNumberVerificationCodeResult:
    out: SendDestinationNumberVerificationCodeResult = {}  # type: ignore[typeddict-item]
    if "MessageId" in data:
        out["message_id"] = data["MessageId"]
    else:
        raise DeserializationError(
            "SendDestinationNumberVerificationCodeResult.message_id required"
        )
    return out
