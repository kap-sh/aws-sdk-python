"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.code_review

CodeReviewList: TypeAlias = list["aws_sdk_securityagent.types.code_review.CodeReview"]


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewList) -> list:
    import aws_sdk_securityagent.types.code_review

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.code_review.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeReviewList:
    import aws_sdk_securityagent.types.code_review

    out: CodeReviewList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.code_review.deserialize_json(item))
    return out
