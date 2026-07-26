"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionDifference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.difference_status
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.question_title


class QuestionDifference(TypedDict, closed=True):
    question_id: NotRequired["capo_wellarchitected.types.question_id.QuestionId"]
    question_title: NotRequired[
        "capo_wellarchitected.types.question_title.QuestionTitle"
    ]
    difference_status: NotRequired[
        "capo_wellarchitected.types.difference_status.DifferenceStatus"
    ]
    """<p>Indicates the type of change to the question.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionDifference) -> dict:
    out: dict = {}
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "question_title" in value:
        out["QuestionTitle"] = value["question_title"]
    if "difference_status" in value:
        import capo_wellarchitected.types.difference_status

        out["DifferenceStatus"] = (
            capo_wellarchitected.types.difference_status.serialize_json(
                value["difference_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> QuestionDifference:
    out: QuestionDifference = {}  # type: ignore[typeddict-item]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "QuestionTitle" in data:
        out["question_title"] = data["QuestionTitle"]
    if "DifferenceStatus" in data:
        import capo_wellarchitected.types.difference_status

        out["difference_status"] = (
            capo_wellarchitected.types.difference_status.deserialize_json(
                data["DifferenceStatus"]
            )
        )
    return out
