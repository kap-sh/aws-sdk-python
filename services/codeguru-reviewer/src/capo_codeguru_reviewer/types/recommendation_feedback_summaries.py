"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RecommendationFeedbackSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.recommendation_feedback_summary

RecommendationFeedbackSummaries: TypeAlias = list[
    "capo_codeguru_reviewer.types.recommendation_feedback_summary.RecommendationFeedbackSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationFeedbackSummaries) -> list:
    import capo_codeguru_reviewer.types.recommendation_feedback_summary

    out: list = []
    for item in value:
        out.append(
            capo_codeguru_reviewer.types.recommendation_feedback_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecommendationFeedbackSummaries:
    import capo_codeguru_reviewer.types.recommendation_feedback_summary

    out: RecommendationFeedbackSummaries = []
    for item in data:
        out.append(
            capo_codeguru_reviewer.types.recommendation_feedback_summary.deserialize_json(
                item
            )
        )
    return out
