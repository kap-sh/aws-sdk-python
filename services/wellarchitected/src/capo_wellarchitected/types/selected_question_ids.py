"""Generated from Smithy shape ``com.amazonaws.wellarchitected#SelectedQuestionIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.selected_question_id

SelectedQuestionIds: TypeAlias = list[
    "capo_wellarchitected.types.selected_question_id.SelectedQuestionId"
]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedQuestionIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SelectedQuestionIds:
    return list(data)
