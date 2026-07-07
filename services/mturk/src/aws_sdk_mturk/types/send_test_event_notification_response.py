"""Generated from Smithy shape ``com.amazonaws.mturk#SendTestEventNotificationResponse``."""

from typing_extensions import TypedDict


class SendTestEventNotificationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendTestEventNotificationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> SendTestEventNotificationResponse:
    out: SendTestEventNotificationResponse = {}  # type: ignore[typeddict-item]
    return out
