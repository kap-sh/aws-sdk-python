"""Generated from Smithy shape ``com.amazonaws.wellarchitected#SelectedPillar``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.pillar_id
    import aws_sdk_wellarchitected.types.selected_question_ids


class SelectedPillar(TypedDict):
    pillar_id: NotRequired["aws_sdk_wellarchitected.types.pillar_id.PillarId"]
    selected_question_ids: NotRequired[
        "aws_sdk_wellarchitected.types.selected_question_ids.SelectedQuestionIds"
    ]
    """<p>Selected question IDs in the selected pillar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectedPillar) -> dict:
    out: dict = {}
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "selected_question_ids" in value:
        import aws_sdk_wellarchitected.types.selected_question_ids

        out["SelectedQuestionIds"] = (
            aws_sdk_wellarchitected.types.selected_question_ids.serialize_json(
                value["selected_question_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelectedPillar:
    out: SelectedPillar = {}  # type: ignore[typeddict-item]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "SelectedQuestionIds" in data:
        import aws_sdk_wellarchitected.types.selected_question_ids

        out["selected_question_ids"] = (
            aws_sdk_wellarchitected.types.selected_question_ids.deserialize_json(
                data["SelectedQuestionIds"]
            )
        )
    return out
