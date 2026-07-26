"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateAnswerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.review_template_answer_summary

ReviewTemplateAnswerSummaries: TypeAlias = list[
    "capo_wellarchitected.types.review_template_answer_summary.ReviewTemplateAnswerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateAnswerSummaries) -> list:
    import capo_wellarchitected.types.review_template_answer_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.review_template_answer_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReviewTemplateAnswerSummaries:
    import capo_wellarchitected.types.review_template_answer_summary

    out: ReviewTemplateAnswerSummaries = []
    for item in data:
        out.append(
            capo_wellarchitected.types.review_template_answer_summary.deserialize_json(
                item
            )
        )
    return out
