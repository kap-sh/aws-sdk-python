"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileQuestionChoices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_choice

ProfileQuestionChoices: TypeAlias = list[
    "capo_wellarchitected.types.profile_choice.ProfileChoice"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQuestionChoices) -> list:
    import capo_wellarchitected.types.profile_choice

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.profile_choice.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileQuestionChoices:
    import capo_wellarchitected.types.profile_choice

    out: ProfileQuestionChoices = []
    for item in data:
        out.append(capo_wellarchitected.types.profile_choice.deserialize_json(item))
    return out
