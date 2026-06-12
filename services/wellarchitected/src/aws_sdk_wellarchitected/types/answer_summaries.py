"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AnswerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.answer_summary

AnswerSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.answer_summary.AnswerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnswerSummaries) -> list:
    import aws_sdk_wellarchitected.types.answer_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_wellarchitected.types.answer_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnswerSummaries:
    import aws_sdk_wellarchitected.types.answer_summary

    out: AnswerSummaries = []
    for item in data:
        out.append(aws_sdk_wellarchitected.types.answer_summary.deserialize_json(item))
    return out
