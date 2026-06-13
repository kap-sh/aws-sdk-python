"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewJobTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_review_job_task

CodeReviewJobTaskList: TypeAlias = list[
    "aws_sdk_securityagent.types.code_review_job_task.CodeReviewJobTask"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewJobTaskList) -> list:
    import aws_sdk_securityagent.types.code_review_job_task

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityagent.types.code_review_job_task.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CodeReviewJobTaskList:
    import aws_sdk_securityagent.types.code_review_job_task

    out: CodeReviewJobTaskList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.code_review_job_task.deserialize_json(item)
        )
    return out
