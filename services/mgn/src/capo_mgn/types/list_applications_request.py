"""Generated from Smithy shape ``com.amazonaws.mgn#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.list_applications_request_filters
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token


class ListApplicationsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_mgn.types.list_applications_request_filters.ListApplicationsRequestFilters"
    ]
    """<p>Applications list filters.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>Maximum results to return when listing applications.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Request next token.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Applications list Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_mgn.types.list_applications_request_filters

        out["filters"] = (
            capo_mgn.types.list_applications_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_mgn.types.list_applications_request_filters

        out["filters"] = (
            capo_mgn.types.list_applications_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
