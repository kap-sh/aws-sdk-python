"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_review_job

CodeReviewJobList: TypeAlias = list[
    "aws_sdk_securityagent.types.code_review_job.CodeReviewJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewJobList) -> list:
    import aws_sdk_securityagent.types.code_review_job

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.code_review_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeReviewJobList:
    import aws_sdk_securityagent.types.code_review_job

    out: CodeReviewJobList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.code_review_job.deserialize_json(item))
    return out
