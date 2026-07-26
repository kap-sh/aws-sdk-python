"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceAnswers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_answer

ChoiceAnswers: TypeAlias = list["capo_wellarchitected.types.choice_answer.ChoiceAnswer"]


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceAnswers) -> list:
    import capo_wellarchitected.types.choice_answer

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.choice_answer.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChoiceAnswers:
    import capo_wellarchitected.types.choice_answer

    out: ChoiceAnswers = []
    for item in data:
        out.append(capo_wellarchitected.types.choice_answer.deserialize_json(item))
    return out
