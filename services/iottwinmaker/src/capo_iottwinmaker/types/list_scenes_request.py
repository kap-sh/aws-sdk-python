"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListScenesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.max_results
    import capo_iottwinmaker.types.next_token


class ListScenesRequest(TypedDict, closed=True):
    workspace_id: "capo_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace that contains the scenes.</p>"""
    max_results: NotRequired["capo_iottwinmaker.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of results to display.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScenesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScenesRequest:
    out: ListScenesRequest = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
