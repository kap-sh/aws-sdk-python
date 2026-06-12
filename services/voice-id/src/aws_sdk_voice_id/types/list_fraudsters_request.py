"""Generated from Smithy shape ``com.amazonaws.voiceid#ListFraudstersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.max_results_for_list
    import aws_sdk_voice_id.types.next_token
    import aws_sdk_voice_id.types.watchlist_id


class ListFraudstersRequest(TypedDict):
    domain_id: "aws_sdk_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain. </p>"""
    watchlist_id: NotRequired["aws_sdk_voice_id.types.watchlist_id.WatchlistId"]
    """<p>The identifier of the watchlist. If provided, all fraudsters in the watchlist are listed. If not provided, all fraudsters in the domain are listed.</p>"""
    max_results: NotRequired[
        "aws_sdk_voice_id.types.max_results_for_list.MaxResultsForList"
    ]
    """<p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>"""
    next_token: NotRequired["aws_sdk_voice_id.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFraudstersRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    if "watchlist_id" in value:
        out["WatchlistId"] = value["watchlist_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFraudstersRequest:
    out: ListFraudstersRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("ListFraudstersRequest.domain_id required")
    if "WatchlistId" in data:
        out["watchlist_id"] = data["WatchlistId"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
