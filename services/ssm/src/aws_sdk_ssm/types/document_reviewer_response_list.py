"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentReviewerResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.document_reviewer_response_source

DocumentReviewerResponseList: TypeAlias = list[
    "aws_sdk_ssm.types.document_reviewer_response_source.DocumentReviewerResponseSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentReviewerResponseList) -> list:
    import aws_sdk_ssm.types.document_reviewer_response_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.document_reviewer_response_source.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentReviewerResponseList:
    import aws_sdk_ssm.types.document_reviewer_response_source

    out: DocumentReviewerResponseList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.document_reviewer_response_source.deserialize_aws_json_1_1(
                item
            )
        )
    return out
