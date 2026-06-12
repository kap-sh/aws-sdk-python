"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierSummariesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classifier_summary

DocumentClassifierSummariesList: TypeAlias = list[
    "aws_sdk_comprehend.types.document_classifier_summary.DocumentClassifierSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierSummariesList) -> list:
    import aws_sdk_comprehend.types.document_classifier_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.document_classifier_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DocumentClassifierSummariesList:
    import aws_sdk_comprehend.types.document_classifier_summary

    out: DocumentClassifierSummariesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.document_classifier_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
