"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.count
    import capo_wellarchitected.types.question

QuestionCounts: TypeAlias = dict[
    "capo_wellarchitected.types.question.Question",
    "capo_wellarchitected.types.count.Count",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: QuestionCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_wellarchitected.types.question

        out[capo_wellarchitected.types.question.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> QuestionCounts:
    out: QuestionCounts = {}
    for key, value in data.items():
        import capo_wellarchitected.types.question

        out[capo_wellarchitected.types.question.deserialize_json(key)] = value
    return out
