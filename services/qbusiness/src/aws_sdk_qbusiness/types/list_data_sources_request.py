"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListDataSourcesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.max_results_integer_for_list_data_sources
    import aws_sdk_qbusiness.types.next_token


class ListDataSourcesRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application linked to the data source connectors.</p>"""
    index_id: "aws_sdk_qbusiness.types.index_id.IndexId"
    """<p>The identifier of the index used with one or more data source connectors.</p>"""
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business data source connectors.</p>"""
    max_results: NotRequired[
        "aws_sdk_qbusiness.types.max_results_integer_for_list_data_sources.MaxResultsIntegerForListDataSources"
    ]
    """<p>The maximum number of data source connectors to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataSourcesRequest:
    out: ListDataSourcesRequest = {}  # type: ignore[typeddict-item]
    return out
