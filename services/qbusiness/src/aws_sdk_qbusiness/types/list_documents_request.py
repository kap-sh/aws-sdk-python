"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDocumentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.data_source_ids
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_documents
    import aws_sdk_qbusiness.types.next_token


class ListDocumentsRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application id the documents are attached to.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index the documents are attached to.</p>"""
    data_source_ids: NotRequired[
        "aws_sdk_qbusiness.types.data_source_ids.DataSourceIds"
    ]
    """<p>The identifier of the data sources the documents are attached to.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of documents.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_documents.MaxResultsIntegerForListDocuments"
    ]
    """<p>The maximum number of documents to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDocumentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDocumentsRequest:
    out: ListDocumentsRequest = {}  # type: ignore[typeddict-item]
    return out
