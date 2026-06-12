"""Generated from Smithy shape ``com.amazonaws.wellarchitected#QuestionCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.count
    import aws_sdk_wellarchitected.types.question

QuestionCounts: TypeAlias = dict[
    "aws_sdk_wellarchitected.types.question.Question",
    "aws_sdk_wellarchitected.types.count.Count",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: QuestionCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_wellarchitected.types.question

        out[aws_sdk_wellarchitected.types.question.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> QuestionCounts:
    out: QuestionCounts = {}
    for key, value in data.items():
        import aws_sdk_wellarchitected.types.question

        out[aws_sdk_wellarchitected.types.question.deserialize_json(key)] = value
    return out
