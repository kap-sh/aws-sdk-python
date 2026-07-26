"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviewCommentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.document_review_comment_source

DocumentReviewCommentList: TypeAlias = list[
    "capo_ssm.types.document_review_comment_source.DocumentReviewCommentSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReviewCommentList) -> list:
    import capo_ssm.types.document_review_comment_source

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.document_review_comment_source.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentReviewCommentList:
    import capo_ssm.types.document_review_comment_source

    out: DocumentReviewCommentList = []
    for item in data:
        out.append(
            capo_ssm.types.document_review_comment_source.deserialize_aws_json_1_1(item)
        )
    return out
