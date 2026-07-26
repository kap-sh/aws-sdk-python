"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#CodeReviewSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.code_review_summary

CodeReviewSummaries: TypeAlias = list[
    "capo_codeguru_reviewer.types.code_review_summary.CodeReviewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewSummaries) -> list:
    import capo_codeguru_reviewer.types.code_review_summary

    out: list = []
    for item in value:
        out.append(
            capo_codeguru_reviewer.types.code_review_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CodeReviewSummaries:
    import capo_codeguru_reviewer.types.code_review_summary

    out: CodeReviewSummaries = []
    for item in data:
        out.append(
            capo_codeguru_reviewer.types.code_review_summary.deserialize_json(item)
        )
    return out
