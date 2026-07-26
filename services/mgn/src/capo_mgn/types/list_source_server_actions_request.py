"""Generated from Smithy shape ``com.amazonaws.mgn#ListSourceServerActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.source_server_actions_request_filters
    import capo_mgn.types.source_server_id


class ListSourceServerActionsRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>Source server ID.</p>"""
    filters: NotRequired[
        "capo_mgn.types.source_server_actions_request_filters.SourceServerActionsRequestFilters"
    ]
    """<p>Filters to apply when listing source server post migration custom actions.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>Maximum amount of items to return when listing source server post migration custom actions.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Next token to use when listing source server post migration custom actions.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID to return when listing source server post migration custom actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceServerActionsRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "filters" in value:
        import capo_mgn.types.source_server_actions_request_filters

        out["filters"] = (
            capo_mgn.types.source_server_actions_request_filters.serialize_json(
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


def deserialize_json(data: dict) -> ListSourceServerActionsRequest:
    out: ListSourceServerActionsRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "ListSourceServerActionsRequest.source_server_id required"
        )
    if "filters" in data:
        import capo_mgn.types.source_server_actions_request_filters

        out["filters"] = (
            capo_mgn.types.source_server_actions_request_filters.deserialize_json(
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
