"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileQuestionChoices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_choice

ProfileQuestionChoices: TypeAlias = list[
    "aws_sdk_wellarchitected.types.profile_choice.ProfileChoice"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileQuestionChoices) -> list:
    import aws_sdk_wellarchitected.types.profile_choice

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.profile_choice.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProfileQuestionChoices:
    import aws_sdk_wellarchitected.types.profile_choice

    out: ProfileQuestionChoices = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.profile_choice.deserialize_json(item))
    return out
