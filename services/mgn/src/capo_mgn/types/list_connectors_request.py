"""Generated from Smithy shape ``com.amazonaws.mgn#ListConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.list_connectors_request_filters
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token


class ListConnectorsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_mgn.types.list_connectors_request_filters.ListConnectorsRequestFilters"
    ]
    """<p>List Connectors Request filters.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>List Connectors Request max results.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>List Connectors Request next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_mgn.types.list_connectors_request_filters

        out["filters"] = capo_mgn.types.list_connectors_request_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectorsRequest:
    out: ListConnectorsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_mgn.types.list_connectors_request_filters

        out["filters"] = (
            capo_mgn.types.list_connectors_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
