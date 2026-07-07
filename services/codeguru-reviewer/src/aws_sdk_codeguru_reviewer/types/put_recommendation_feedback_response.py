"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#PutRecommendationFeedbackResponse``."""

from typing_extensions import TypedDict


class PutRecommendationFeedbackResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutRecommendationFeedbackResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutRecommendationFeedbackResponse:
    out: PutRecommendationFeedbackResponse = {}  # type: ignore[typeddict-item]
    return out
