"""Generated from Smithy shape ``com.amazonaws.wellarchitected#SelectedPillar``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.selected_question_ids


class SelectedPillar(TypedDict, closed=True):
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    selected_question_ids: NotRequired[
        "capo_wellarchitected.types.selected_question_ids.SelectedQuestionIds"
    ]
    """<p>Selected question IDs in the selected pillar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectedPillar) -> dict:
    out: dict = {}
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "selected_question_ids" in value:
        import capo_wellarchitected.types.selected_question_ids

        out["SelectedQuestionIds"] = (
            capo_wellarchitected.types.selected_question_ids.serialize_json(
                value["selected_question_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelectedPillar:
    out: SelectedPillar = {}  # type: ignore[typeddict-item]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "SelectedQuestionIds" in data:
        import capo_wellarchitected.types.selected_question_ids

        out["selected_question_ids"] = (
            capo_wellarchitected.types.selected_question_ids.deserialize_json(
                data["SelectedQuestionIds"]
            )
        )
    return out
