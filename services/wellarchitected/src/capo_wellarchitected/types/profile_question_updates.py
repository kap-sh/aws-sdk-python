"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileQuestionUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_question_update

ProfileQuestionUpdates: TypeAlias = list[
    "capo_wellarchitected.types.profile_question_update.ProfileQuestionUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQuestionUpdates) -> list:
    import capo_wellarchitected.types.profile_question_update

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.profile_question_update.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProfileQuestionUpdates:
    import capo_wellarchitected.types.profile_question_update

    out: ProfileQuestionUpdates = []
    for item in data:
        out.append(
            capo_wellarchitected.types.profile_question_update.deserialize_json(item)
        )
    return out
