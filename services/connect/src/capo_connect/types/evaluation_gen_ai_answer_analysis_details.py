"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationGenAIAnswerAnalysisDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_suggested_answer_justification
    import capo_connect.types.evaluation_transcript_points_of_interest


class EvaluationGenAIAnswerAnalysisDetails(TypedDict, closed=True):
    justification: NotRequired[
        "capo_connect.types.evaluation_suggested_answer_justification.EvaluationSuggestedAnswerJustification"
    ]
    """<p>Generative AI automation answer justification.</p>"""
    points_of_interest: NotRequired[
        "capo_connect.types.evaluation_transcript_points_of_interest.EvaluationTranscriptPointsOfInterest"
    ]
    """<p>Generative AI automation answer analysis points of interest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationGenAIAnswerAnalysisDetails) -> dict:
    out: dict = {}
    if "justification" in value:
        out["Justification"] = value["justification"]
    if "points_of_interest" in value:
        import capo_connect.types.evaluation_transcript_points_of_interest

        out["PointsOfInterest"] = (
            capo_connect.types.evaluation_transcript_points_of_interest.serialize_json(
                value["points_of_interest"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationGenAIAnswerAnalysisDetails:
    out: EvaluationGenAIAnswerAnalysisDetails = {}  # type: ignore[typeddict-item]
    if "Justification" in data:
        out["justification"] = data["Justification"]
    if "PointsOfInterest" in data:
        import capo_connect.types.evaluation_transcript_points_of_interest

        out["points_of_interest"] = (
            capo_connect.types.evaluation_transcript_points_of_interest.deserialize_json(
                data["PointsOfInterest"]
            )
        )
    return out
