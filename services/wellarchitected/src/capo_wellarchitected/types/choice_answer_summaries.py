"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ChoiceAnswerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.choice_answer_summary

ChoiceAnswerSummaries: TypeAlias = list[
    "capo_wellarchitected.types.choice_answer_summary.ChoiceAnswerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChoiceAnswerSummaries) -> list:
    import capo_wellarchitected.types.choice_answer_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.choice_answer_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChoiceAnswerSummaries:
    import capo_wellarchitected.types.choice_answer_summary

    out: ChoiceAnswerSummaries = []
    for item in data:
        out.append(
            capo_wellarchitected.types.choice_answer_summary.deserialize_json(item)
        )
    return out
