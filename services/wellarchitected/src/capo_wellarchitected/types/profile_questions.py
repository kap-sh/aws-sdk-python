"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileQuestions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_question

ProfileQuestions: TypeAlias = list[
    "capo_wellarchitected.types.profile_question.ProfileQuestion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQuestions) -> list:
    import capo_wellarchitected.types.profile_question

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.profile_question.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileQuestions:
    import capo_wellarchitected.types.profile_question

    out: ProfileQuestions = []
    for item in data:
        out.append(capo_wellarchitected.types.profile_question.deserialize_json(item))
    return out
