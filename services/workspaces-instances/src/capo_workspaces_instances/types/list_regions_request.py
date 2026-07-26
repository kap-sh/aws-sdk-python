"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListRegionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.max_results
    import capo_workspaces_instances.types.next_token


class ListRegionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_workspaces_instances.types.max_results.MaxResults"]
    """<p>Maximum number of regions to return in a single API call. Enables pagination of region results.</p>"""
    next_token: NotRequired["capo_workspaces_instances.types.next_token.NextToken"]
    """<p>Pagination token for retrieving subsequent pages of region results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRegionsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRegionsRequest:
    out: ListRegionsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
