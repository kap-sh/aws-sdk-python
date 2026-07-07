"""Generated from Smithy shape ``com.amazonaws.codeartifact#ListDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.list_domains_max_results
    import aws_sdk_codeartifact.types.pagination_token


class ListDomainsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_codeartifact.types.list_domains_max_results.ListDomainsMaxResults"
    ]
    """<p> The maximum number of results to return per page. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeartifact.types.pagination_token.PaginationToken"
    ]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainsRequest:
    out: ListDomainsRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
