"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.code_review_summary

CodeReviewSummaryList: TypeAlias = list[
    "capo_securityagent.types.code_review_summary.CodeReviewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewSummaryList) -> list:
    import capo_securityagent.types.code_review_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.code_review_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeReviewSummaryList:
    import capo_securityagent.types.code_review_summary

    out: CodeReviewSummaryList = []
    for item in data:
        out.append(capo_securityagent.types.code_review_summary.deserialize_json(item))
    return out
