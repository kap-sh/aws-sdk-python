"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.best_practices
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.risk


class QuestionMetric(TypedDict, closed=True):
    question_id: NotRequired["capo_wellarchitected.types.question_id.QuestionId"]
    risk: NotRequired["capo_wellarchitected.types.risk.Risk"]
    best_practices: NotRequired[
        "capo_wellarchitected.types.best_practices.BestPractices"
    ]
    """<p>The best practices, or choices, that have been identified as contributing to risk in a question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionMetric) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "risk" in value:
        import capo_wellarchitected.types.risk

        out["Risk"] = capo_wellarchitected.types.risk.serialize_json(value["risk"])
    if "best_practices" in value:
        import capo_wellarchitected.types.best_practices

        out["BestPractices"] = capo_wellarchitected.types.best_practices.serialize_json(
            value["best_practices"]
        )
    return out


def deserialize_json(data: dict) -> QuestionMetric:
    out: QuestionMetric = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "Risk" in data:
        import capo_wellarchitected.types.risk

        out["risk"] = capo_wellarchitected.types.risk.deserialize_json(data["Risk"])
    if "BestPractices" in data:
        import capo_wellarchitected.types.best_practices

        out["best_practices"] = (
            capo_wellarchitected.types.best_practices.deserialize_json(
                data["BestPractices"]
            )
        )
    return out
