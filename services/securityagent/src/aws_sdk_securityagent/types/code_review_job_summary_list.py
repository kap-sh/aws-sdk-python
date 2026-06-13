"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_review_job_summary

CodeReviewJobSummaryList: TypeAlias = list[
    "aws_sdk_securityagent.types.code_review_job_summary.CodeReviewJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewJobSummaryList) -> list:
    import aws_sdk_securityagent.types.code_review_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityagent.types.code_review_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CodeReviewJobSummaryList:
    import aws_sdk_securityagent.types.code_review_job_summary

    out: CodeReviewJobSummaryList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.code_review_job_summary.deserialize_json(item)
        )
    return out
