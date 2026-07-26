"""Generated from Smithy shape ``com.amazonaws.detective#ListGraphsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_list
    import capo_detective.types.pagination_token


class ListGraphsResponse(TypedDict, closed=True):
    graph_list: NotRequired["capo_detective.types.graph_list.GraphList"]
    """<p>A list of behavior graphs that the account is an administrator account for.</p>"""
    next_token: NotRequired["capo_detective.types.pagination_token.PaginationToken"]
    """<p>If there are more behavior graphs remaining in the results, then this is the pagination token to use to request the next page of behavior graphs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGraphsResponse) -> dict:
    out: dict = {}
    if "graph_list" in value:
        import capo_detective.types.graph_list

        out["GraphList"] = capo_detective.types.graph_list.serialize_json(
            value["graph_list"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGraphsResponse:
    out: ListGraphsResponse = {}  # type: ignore[typeddict-item]
    if "GraphList" in data:
        import capo_detective.types.graph_list

        out["graph_list"] = capo_detective.types.graph_list.deserialize_json(
            data["GraphList"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
