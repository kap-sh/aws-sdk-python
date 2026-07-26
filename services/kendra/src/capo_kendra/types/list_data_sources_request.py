"""Generated from Smithy shape ``com.amazonaws.kendra#ListDataSourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.index_id
    import capo_kendra.types.max_results_integer_for_list_data_sources_request
    import capo_kendra.types.next_token


class ListDataSourcesRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index used with one or more data source connectors.</p>"""
    next_token: NotRequired["capo_kendra.types.next_token.NextToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of data source connectors. </p>"""
    max_results: NotRequired[
        "capo_kendra.types.max_results_integer_for_list_data_sources_request.MaxResultsIntegerForListDataSourcesRequest"
    ]
    """<p>The maximum number of data source connectors to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDataSourcesRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDataSourcesRequest:
    out: ListDataSourcesRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("ListDataSourcesRequest.index_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
