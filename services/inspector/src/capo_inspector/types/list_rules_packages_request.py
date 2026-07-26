"""Generated from Smithy shape ``com.amazonaws.inspector#ListRulesPackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.list_max_results
    import capo_inspector.types.pagination_token


class ListRulesPackagesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the <b>ListRulesPackages</b> action. Subsequent calls to the action fill <b>nextToken</b> in the request with the value of <b>NextToken</b> from the previous response to continue listing data.</p>"""
    max_results: NotRequired["capo_inspector.types.list_max_results.ListMaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 10. The maximum value is 500.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRulesPackagesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRulesPackagesRequest:
    out: ListRulesPackagesRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
