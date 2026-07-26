"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplatePillarReviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.notes
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.pillar_name
    import capo_wellarchitected.types.question_counts


class ReviewTemplatePillarReviewSummary(TypedDict, closed=True):
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    pillar_name: NotRequired["capo_wellarchitected.types.pillar_name.PillarName"]
    notes: NotRequired["capo_wellarchitected.types.notes.Notes"]
    question_counts: NotRequired[
        "capo_wellarchitected.types.question_counts.QuestionCounts"
    ]
    """<p>A count of how many questions are answered and unanswered in the requested pillar of the lens review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplatePillarReviewSummary) -> dict:
    out: dict = {}
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "pillar_name" in value:
        out["PillarName"] = value["pillar_name"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "question_counts" in value:
        import capo_wellarchitected.types.question_counts

        out["QuestionCounts"] = (
            capo_wellarchitected.types.question_counts.serialize_json(
                value["question_counts"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReviewTemplatePillarReviewSummary:
    out: ReviewTemplatePillarReviewSummary = {}  # type: ignore[typeddict-item]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "PillarName" in data:
        out["pillar_name"] = data["PillarName"]
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "QuestionCounts" in data:
        import capo_wellarchitected.types.question_counts

        out["question_counts"] = (
            capo_wellarchitected.types.question_counts.deserialize_json(
                data["QuestionCounts"]
            )
        )
    return out
