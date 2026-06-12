"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileQuestionUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_question_update

ProfileQuestionUpdates: TypeAlias = list[
    "aws_sdk_wellarchitected.types.profile_question_update.ProfileQuestionUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQuestionUpdates) -> list:
    import aws_sdk_wellarchitected.types.profile_question_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.profile_question_update.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProfileQuestionUpdates:
    import aws_sdk_wellarchitected.types.profile_question_update

    out: ProfileQuestionUpdates = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.profile_question_update.deserialize_json(item)
        )
    return out
