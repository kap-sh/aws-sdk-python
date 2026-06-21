"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviewAction``."""

from typing import Literal, TypeAlias, cast

DocumentReviewAction: TypeAlias = Literal[
    "SendForReview",
    "UpdateReview",
    "Approve",
    "Reject",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReviewAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReviewAction:
    return cast(DocumentReviewAction, data)
