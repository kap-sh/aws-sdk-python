"""Generated from Smithy shape ``com.amazonaws.securityir#SendFeedbackResponse``."""

from typing_extensions import TypedDict


class SendFeedbackResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendFeedbackResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendFeedbackResponse:
    out: SendFeedbackResponse = {}  # type: ignore[typeddict-item]
    return out
