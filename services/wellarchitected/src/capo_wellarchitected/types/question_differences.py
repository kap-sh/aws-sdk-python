"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionDifferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.question_difference

QuestionDifferences: TypeAlias = list[
    "capo_wellarchitected.types.question_difference.QuestionDifference"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuestionDifferences) -> list:
    import capo_wellarchitected.types.question_difference

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.question_difference.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuestionDifferences:
    import capo_wellarchitected.types.question_difference

    out: QuestionDifferences = []
    for item in data:
        out.append(
            capo_wellarchitected.types.question_difference.deserialize_json(item)
        )
    return out
