"""Generated from Smithy shape ``com.amazonaws.simpledbv2#ListExportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_simpledbv2.types.domain_name
    import aws_sdk_simpledbv2.types.max_results
    import aws_sdk_simpledbv2.types.next_token


class ListExportsRequest(TypedDict, closed=True):
    domain_name: NotRequired["aws_sdk_simpledbv2.types.domain_name.DomainName"]
    """The name of the domain to filter exports. If not provided, exports for all the domains will be listed."""
    max_results: NotRequired["aws_sdk_simpledbv2.types.max_results.MaxResults"]
    """The maximum number of exports to return in a single response."""
    next_token: NotRequired["aws_sdk_simpledbv2.types.next_token.NextToken"]
    """A pagination token used to retrieve the next page of results. This token is obtained from the nextToken field in the previous ListExportsResponse. Leave empty for the first request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportsRequest) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExportsRequest:
    out: ListExportsRequest = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
