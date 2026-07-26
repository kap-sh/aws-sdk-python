"""Generated from Smithy shape ``com.amazonaws.wellarchitected#SelectedChoiceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_id

SelectedChoiceIds: TypeAlias = list["capo_wellarchitected.types.choice_id.ChoiceId"]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedChoiceIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SelectedChoiceIds:
    return list(data)
