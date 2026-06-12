"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileQuestions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_question

ProfileQuestions: TypeAlias = list[
    "aws_sdk_wellarchitected.types.profile_question.ProfileQuestion"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQuestions) -> list:
    import aws_sdk_wellarchitected.types.profile_question

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.profile_question.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileQuestions:
    import aws_sdk_wellarchitected.types.profile_question

    out: ProfileQuestions = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.profile_question.deserialize_json(item)
        )
    return out
