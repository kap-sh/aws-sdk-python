"""Generated from Smithy shape ``com.amazonaws.comprehend#ListDocumentClassifierSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.document_classifier_summaries_list
    import aws_sdk_comprehend.types.string


class ListDocumentClassifierSummariesResponse(TypedDict, closed=True):
    document_classifier_summaries_list: NotRequired[
        "aws_sdk_comprehend.types.document_classifier_summaries_list.DocumentClassifierSummariesList"
    ]
    """<p>The list of summaries of document classifiers.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDocumentClassifierSummariesResponse) -> dict:
    out: dict = {}
    if "document_classifier_summaries_list" in value:
        import aws_sdk_comprehend.types.document_classifier_summaries_list

        out["DocumentClassifierSummariesList"] = (
            aws_sdk_comprehend.types.document_classifier_summaries_list.serialize_aws_json_1_1(
                value["document_classifier_summaries_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDocumentClassifierSummariesResponse:
    out: ListDocumentClassifierSummariesResponse = {}  # type: ignore[typeddict-item]
    if "DocumentClassifierSummariesList" in data:
        import aws_sdk_comprehend.types.document_classifier_summaries_list

        out["document_classifier_summaries_list"] = (
            aws_sdk_comprehend.types.document_classifier_summaries_list.deserialize_aws_json_1_1(
                data["DocumentClassifierSummariesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
