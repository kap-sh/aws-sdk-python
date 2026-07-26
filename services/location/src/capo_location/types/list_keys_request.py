"""Generated from Smithy shape ``com.amazonaws.location#ListKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.api_key_filter
    import capo_location.types.token


class ListKeysRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>"""
    next_token: NotRequired["capo_location.types.token.Token"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>"""
    filter: NotRequired["capo_location.types.api_key_filter.ApiKeyFilter"]
    """<p>Optionally filter the list to only <code>Active</code> or <code>Expired</code> API keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filter" in value:
        import capo_location.types.api_key_filter

        out["Filter"] = capo_location.types.api_key_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ListKeysRequest:
    out: ListKeysRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filter" in data:
        import capo_location.types.api_key_filter

        out["filter"] = capo_location.types.api_key_filter.deserialize_json(
            data["Filter"]
        )
    return out
