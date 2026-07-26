"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarDifference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.difference_status
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.pillar_name
    import capo_wellarchitected.types.question_differences


class PillarDifference(TypedDict, closed=True):
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    pillar_name: NotRequired["capo_wellarchitected.types.pillar_name.PillarName"]
    difference_status: NotRequired[
        "capo_wellarchitected.types.difference_status.DifferenceStatus"
    ]
    """<p>Indicates the type of change to the pillar.</p>"""
    question_differences: NotRequired[
        "capo_wellarchitected.types.question_differences.QuestionDifferences"
    ]
    """<p>List of question differences.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PillarDifference) -> dict:
    out: dict = {}
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "pillar_name" in value:
        out["PillarName"] = value["pillar_name"]
    if "difference_status" in value:
        import capo_wellarchitected.types.difference_status

        out["DifferenceStatus"] = (
            capo_wellarchitected.types.difference_status.serialize_json(
                value["difference_status"]
            )
        )
    if "question_differences" in value:
        import capo_wellarchitected.types.question_differences

        out["QuestionDifferences"] = (
            capo_wellarchitected.types.question_differences.serialize_json(
                value["question_differences"]
            )
        )
    return out


def deserialize_json(data: dict) -> PillarDifference:
    out: PillarDifference = {}  # type: ignore[typeddict-item]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "PillarName" in data:
        out["pillar_name"] = data["PillarName"]
    if "DifferenceStatus" in data:
        import capo_wellarchitected.types.difference_status

        out["difference_status"] = (
            capo_wellarchitected.types.difference_status.deserialize_json(
                data["DifferenceStatus"]
            )
        )
    if "QuestionDifferences" in data:
        import capo_wellarchitected.types.question_differences

        out["question_differences"] = (
            capo_wellarchitected.types.question_differences.deserialize_json(
                data["QuestionDifferences"]
            )
        )
    return out
