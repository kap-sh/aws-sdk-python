"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewJobTaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_review_job_task_summary

CodeReviewJobTaskSummaryList: TypeAlias = list[
    "aws_sdk_securityagent.types.code_review_job_task_summary.CodeReviewJobTaskSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewJobTaskSummaryList) -> list:
    import aws_sdk_securityagent.types.code_review_job_task_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityagent.types.code_review_job_task_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CodeReviewJobTaskSummaryList:
    import aws_sdk_securityagent.types.code_review_job_task_summary

    out: CodeReviewJobTaskSummaryList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.code_review_job_task_summary.deserialize_json(
                item
            )
        )
    return out
