"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviewCommentType``."""

from typing import Literal, TypeAlias, cast

DocumentReviewCommentType: TypeAlias = Literal["Comment",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReviewCommentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentReviewCommentType:
    return cast(DocumentReviewCommentType, data)
