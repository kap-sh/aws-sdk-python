"""Generated from Smithy shape ``com.amazonaws.devopsguru#PutFeedbackResponse``."""

from typing_extensions import TypedDict


class PutFeedbackResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutFeedbackResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutFeedbackResponse:
    out: PutFeedbackResponse = {}  # type: ignore[typeddict-item]
    return out
